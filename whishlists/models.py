from django.db import models


class Wishlist(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Category(models.Model):
    name = models.CharField(max_length=254)
    friendly_name = models.CharField(max_length=254, null=True, blank=True)

    def __str__(self):
        return self.name

    def get_friendly_name(self):
        return self.friendly_name


class Product(models.Model):
    category = models.ForeignKey(
        'Category', null=True, blank=True, on_delete=models.SET_NULL)
    sku = models.CharField(max_length=254, null=True, blank=True)
    name = models.CharField(max_length=254)
    description = models.TextField()
    price = models.DecimalField(max_digits=6, decimal_places=2)
    rating = models.DecimalField(
        max_digits=6, decimal_places=2, null=True, blank=True)
    image_url = models.URLField(max_length=1024, null=True, blank=True)
    image = models.ImageField(null=True, blank=True)

#     def __str__(self):
#         return self.name


# from django.contrib.auth.models import User
# from django.dispatch import receiver #add this
# from django.db.models.signals import post_save #add this

# # Create your models here.
#  ...

# class Profile(models.Model):
# 	user = models.OneToOneField(User, on_delete=models.CASCADE)
# 	products = models.ManyToManyField(Product)

# 	@receiver(post_save, sender=User) #add this
# 	def create_user_profile(sender, instance, created, **kwargs):
# 		if created:
# 			Profile.objects.create(user=instance)

# 	@receiver(post_save, sender=User) #add this
# 	def save_user_profile(sender, instance, **kwargs):
# 		instance.profile.save()


# from django.db import models
# from django.conf import settings
# from django.utils.translation import ugettext as _

# from .settings import wishlist_settings

# from .managers import UserManager


# AUTH_USER_MODEL = getattr(settings, 'AUTH_USER_MODEL', 'auth.User')


# class WishlistItem(models.Model):
#     """ Item in wishlist. """

#     created = models.DateTimeField(_('created'), auto_now_add=True)

#     user = models.ForeignKey(AUTH_USER_MODEL)
#     item = models.ForeignKey(wishlist_settings.ITEM_MODEL)

#     objects = UserManager()

#     class Meta:
#         verbose_name = _('wishlist')
#         verbose_name_plural = _('wishlists')
#         ordering = ['-created']
#         unique_together = ['user', 'item']

#     def __unicode__(self):
#         """ Wrap unicode of item. """

#         assert self.item

#         return unicode(self.item)

#     def get_absolute_url(self):
#         """ Return absolute URL for item. """

#         return self.item.get_absolute_url()
