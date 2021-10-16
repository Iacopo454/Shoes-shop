from django.contrib import admin
from .models import Product, Category, Wishlist

# Register your models here.

class ProductAdmin(admin.ModelAdmin):
    list_display = (
        'sku',
        'name',
        'category',
        'price',
        'rating',
        'image',
    )

    ordering = ('sku',)

class WishlistAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )


admin.site.register(Wishlist, WishlistAdmin)
admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)
















# from django.contrib import admin

# # Register your models here.
# from .models import WishlistItem


# class WishlistItemAdmin(admin.ModelAdmin):
#     """ Admin for WishlistItem. """

#     pass

# admin.site.register(WishlistItem, WishlistItemAdmin)


