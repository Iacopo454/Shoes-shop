from django.db import models
from django.contrib.auth.models import User
from products.models import Product


class UserWishlist(models.Model):
    """
    A user wishlist model for storing user product wishlist
    """
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='wishlist_product')
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user} - {self.product}"