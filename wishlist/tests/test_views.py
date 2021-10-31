from django.contrib.auth import get_user_model
from django.test import TestCase
from wishlist.models import UserWishlist

from django.urls import reverse

User = get_user_model()

WISHLIST_URL = reverse('wishlist:index')
ADD_TO_WISHLIST_URL = reverse('wishlist:add_to_wishlist', kwargs={'product_id': 1})
PRODUCT_DETAILS_URL = reverse('product_detail', kwargs={'product_id': 1})


class PublicWishlistViewsTest(TestCase):
    """ Test the publicly available wishlist. """

    def test_login_required_wishlist(self):
        """Test that login is required for retrieving wishlist"""

        res = self.client.get(WISHLIST_URL)
        self.assertEqual(res.status_code, 302)

    def test_login_required_add_to_wishlist(self):
        """Test that login is required for add product into wishlist"""

        res = self.client.get(ADD_TO_WISHLIST_URL)
        self.assertEqual(res.status_code, 302)


class PrivateWishlistViewsTest(TestCase):
    """ Test the authorized user wishlist. """

    fixtures = ['categories.json', 'products.json', ]

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

        UserWishlist.objects.create(user=test_user, product_id=1)

    def test_retrieve_wishlist(self):
        """Test retrieving user wishlist"""

        res = self.client.get(WISHLIST_URL)

        user_wishlist = UserWishlist.objects.all()
        self.assertEqual(res.status_code, 200)
        self.assertEqual(user_wishlist.count(), 1)

    def test_add_to_wishlist(self):
        """Test add to wishlist view"""

        wishlist = self.client.post(ADD_TO_WISHLIST_URL, {
            "product_id": 1
            }, HTTP_REFERER=PRODUCT_DETAILS_URL)

        self.assertRedirects(wishlist, PRODUCT_DETAILS_URL)