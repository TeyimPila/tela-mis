from django.contrib import admin
from .models import Product
from import_export.admin import ImportExportActionModelAdmin


# Register your models here.
class ProductAdmin(ImportExportActionModelAdmin):
    list_display = (
        'name', 'description', 'category', 'purchased', 'date_added', 'last_updated', 'ok', 'damaged', 'out', 'at_hand',
        'available',)
    fields = ['name', 'image', 'description', 'category', 'purchased','available']
    search_fields = ('name', 'category', 'available')
    ordering = ['name', 'category']
    list_filter = ('category', 'date_added', 'last_updated', 'available')


admin.site.register(Product, ProductAdmin)
