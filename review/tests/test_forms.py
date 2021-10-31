from django.test import TestCase
from review.models import ReviewRating
from review.forms import ReviewForm


class ReviewFormTest(TestCase):
    """ Unit test for review form. """

    fixtures = ['categories.json', 'products.json', 'orders.json', ]

    def test_review_form_is_invalid(self):
        form = ReviewForm(data={"order_item": "1", "rating": "5"})
        self.assertFalse(form.is_valid())

    def test_review_form_is_valid(self):
        form = ReviewForm(data={"order_item": "1", "rating": "5", "review": "Good product"})
        print(form.errors)
        self.assertTrue(form.is_valid())