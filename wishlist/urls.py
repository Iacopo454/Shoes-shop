from django.urls import path
from . import views

app_name = 'wishlist'

urlpatterns = [
    path('', views.wishlist_view, name='index'),
    path('<int:product_id>/', views.add_to_wishlist, name='add_to_wishlist'),
]