from django.test import TestCase
from wishlist.models import UserWishlist


class UserWishlistModelTest(TestCase):
    """ Unit test for UserWishlist model. """

    fixtures = ['categories.json', 'products.json', 'users.json', ]

    def setUp(self):
        UserWishlist.objects.create(
            user_id=1, product_id=1
        )

    def test_create_wishlist(self):
        """Favourite product that can saved into database"""

        wishlist = UserWishlist.objects.get(user_id=1)
        self.assertEqual(wishlist.product_id, 1)