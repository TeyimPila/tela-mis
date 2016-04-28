from django.contrib import admin
from .models import Checkout, CheckoutItem
from genericadmin.admin import GenericAdminModelAdmin


# Register your models here.

class CheckoutItemInline(admin.TabularInline):
    model = CheckoutItem
    # raw_id_fields = ['product', 'checkout']


class CheckoutAdmin(GenericAdminModelAdmin):
    list_display = ['id', 'content_type', 'object_id', 'checkout_date', 'updated', 'check_in_complete']
    list_filter = ['content_type', 'checkout_date', 'updated', 'check_in_complete']
    search_fields = ['content_type', ]
    # raw_id_fields = ['object_id', ]
    inlines = [CheckoutItemInline]


class CheckoutItemAdmin(admin.ModelAdmin):
    list_display = ['id', 'product', 'status', 'quantity']
    # fields = []


admin.site.register(Checkout, CheckoutAdmin)
admin.site.register(CheckoutItem, CheckoutItemAdmin)
