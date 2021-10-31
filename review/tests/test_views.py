from django.contrib.auth import get_user_model
from django.test import TestCase
from review.models import ReviewRating
from checkout.models import Order, OrderLineItem
from django.urls import reverse

User = get_user_model()

ORDER_VIEW_URL = reverse('review:index')
SUBMIT_REVIEW_URL = reverse('review:submit_review')
ORDER_DETAILS_URL = reverse('review:order_details', kwargs={'order_number': 1})


class PublicReviewViewsTest(TestCase):
    """ Test the publicly available orders and submit review. """

    def test_login_required_order_view(self):
        """Test that login is required for retrieving orders"""

        res = self.client.get(ORDER_VIEW_URL)
        self.assertEqual(res.status_code, 302)

    def test_login_required_order_details(self):
        """Test that login is required for order details page"""

        res = self.client.get(ORDER_DETAILS_URL)
        self.assertEqual(res.status_code, 302)

    def test_login_required_review(self):
        """Test that login is required for submit a review"""

        res = self.client.get(SUBMIT_REVIEW_URL)
        self.assertEqual(res.status_code, 302)


class PrivateReviewViewsTest(TestCase):
    """ Test the authorized user orders and submit review. """

    fixtures = ['categories.json', 'products.json', 'orders.json', ]

    def setUp(self):
        user_data = {
            'username': 'test',
            'email': 'test@gmail.com', 
            'password': 'test123456'
            }
        test_user = User.objects.create_user(**user_data)
        test_user.set_password(user_data.get('password'))

        self.login = self.client.login(
            email=user_data.get('email'), 
            password=user_data.get('password')
        )

    def test_retrieve_orders(self):
        """Test retrieving orders"""

        res = self.client.get(ORDER_VIEW_URL)

        orders = Order.objects.all()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(orders.count(), 1)

    def test_orders_details(self):
        """Test order details view"""

        res = self.client.get(ORDER_DETAILS_URL)

        order_item = OrderLineItem.objects.filter(order_id=1)
        self.assertEqual(res.status_code, 200)
        self.assertEqual(order_item.count(), 1)

    def test_submit_review(self):
        """ Test submit review function """

        review = self.client.post(SUBMIT_REVIEW_URL, {
            "order_item": 1, "rating": 5, "review": "Good Products"
            }, HTTP_REFERER=ORDER_DETAILS_URL)

        self.assertRedirects(review, ORDER_DETAILS_URL)