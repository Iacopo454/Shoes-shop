boutique_ado_v1/products/admin.py /
@ckz8780
ckz8780 Customized admin
Latest commit 1033bd2 on 31 Jan 2020
 History
 1 contributor
25 lines (20 sloc)  492 Bytes
  
from django.contrib import admin
from .models import Product, Category

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

class CategoryAdmin(admin.ModelAdmin):
    list_display = (
        'friendly_name',
        'name',
    )

admin.site.register(Product, ProductAdmin)
admin.site.register(Category, CategoryAdmin)

