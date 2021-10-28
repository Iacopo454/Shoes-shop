from django.db.models import Avg
from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from checkout.models import Order, OrderLineItem
from review.models import ReviewRating
from products.models import Product, Category

from review.forms import ReviewForm


@login_required
def order_view(request):
    """Show all orders for the requested user"""

    orders = Order.objects.filter(user_profile__user=request.user).order_by('-id')
    return render(request, "review/order_list.html", {"orders": orders, 'categories': Category.objects.all()})

@login_required
def order_details(request, order_number):
    """A view to show the details of a specific order"""

    order_item = OrderLineItem.objects.filter(order__order_number=order_number, order__user_profile__user=request.user)
    return render(request, "review/order_details.html", {"order_item": order_item, 'categories': Category.objects.all()})

@login_required
def submit_review(request):
    """A view to submit a review"""

    url = request.META.get('HTTP_REFERER')
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            data = ReviewRating(
                order_item= form.cleaned_data['order_item'], 
                rating= form.cleaned_data['rating'], 
                review= form.cleaned_data['review']
            )
            data.save()

            # calculate review of the product
            # and save into product model
            avg_rating = ReviewRating.objects.filter(order_item__product=data.order_item.product).annotate(ave_price=Avg('rating'))
            Product.objects.filter(pk=data.order_item.product.id).update(rating=avg_rating[0].rating)

            messages.success(request, 'Thank you! Your review has been submitted.')
            return redirect(url)