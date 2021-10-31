from django.contrib import messages
from django.http import HttpResponseRedirect
from django.shortcuts import render, get_object_or_404
from django.contrib.auth.decorators import login_required
from products.models import Product, Category
from wishlist.models import UserWishlist


@login_required
def wishlist_view(request):
    """Show all product of wishlist for the requested user"""

    user_wishlist = UserWishlist.objects.filter(user=request.user)
    return render(request, "wishlist/user_wishlist.html", {
        "user_wishlist": user_wishlist, 
        "categories": Category.objects.all()
        })


@login_required
def add_to_wishlist(request, product_id):
    """A view to add or remove from wishlist"""
       
    product = get_object_or_404(Product, id=product_id) 
    user_wishlist = product.wishlist_product.filter(user=request.user) 

    if user_wishlist.exists():
        user_wishlist.delete()
        msg = f"{product} has been removed from your WishList"
        messages.error(request, msg)
    else:        
        wishlist = UserWishlist(user=request.user, product=product)
        wishlist.save()  
        msg = f"Added {product} to your WishList"      
        messages.success(request, msg)

    return HttpResponseRedirect(request.META["HTTP_REFERER"])