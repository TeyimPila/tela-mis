from django.contrib import admin
from .models import Product
from import_export.admin import ImportExportActionModelAdmin


# Register your models here.
class ProductAdmin(ImportExportActionModelAdmin):
    list_display = (
        'item', 'description', 'category', 'purchased', 'date_added', 'last_updated', 'ok', 'damaged', 'out', 'at_hand',
        'still_available',)
    fields = ['item', 'description', 'category', 'purchased']
    search_fields = ('item', 'category', 'still_available')
    ordering = ['item', 'category']
    list_filter = ('category', 'date_added', 'last_updated', 'still_available')


admin.site.register(Product, ProductAdmin)
