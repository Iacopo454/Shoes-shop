from django.db import models
from django.contrib.auth.models import User
from products.models import Product
from checkout.models import OrderLineItem


class ReviewRating(models.Model):
    """
    A user review rating model
    """ 
    order_item = models.ForeignKey(OrderLineItem, on_delete=models.CASCADE, related_name='review_order_item')
    rating = models.IntegerField()
    review = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.order_item} - {self.rating}'