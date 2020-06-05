from django.contrib import admin
from . import models

# Register your models here.


class ImageInline(admin.TabularInline):
    model = models.Image
    row_id_fields = ['image']


@admin.register(models.Product)
class ProductAdmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'vendor_id', 'price', 'sale_price', 'badges',
                    'category_id', 'num_stock', 'num_views', 'num_purchases', 'num_added_cart', 'status']
    list_filter = ['created_date', 'modify_date', 'status', 'badges']
    list_editable = ['price', 'sale_price', 'status']
    inlines = [ImageInline]


admin.site.register(models.Image)
