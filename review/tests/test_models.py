from django.test import TestCase
from review.models import ReviewRating


class ReviewRatingModelTest(TestCase):
    """ Unit test for review rating model. """

    fixtures = ['categories.json', 'products.json', 'orders.json', ]

    def setUp(self):
        ReviewRating.objects.create(
            order_item_id=1, rating=5, review="Good product"
        )

    def test_create_review(self):
        """Review that can saved into database"""

        review = ReviewRating.objects.get(order_item=1)
        self.assertEqual(review.rating, 5)
        self.assertEqual(review.review, 'Good product')