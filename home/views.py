from django.shortcuts import render
from django.conf import settings
from products.models import Category

# Create your views here.
def index(request):
    """ A view to return the index page """
    check = settings.STRIPE_SECRET_KEY
    print(check)
    print("testing")

    return render(request, 'home/index.html', {'categories': Category.objects.all()})
