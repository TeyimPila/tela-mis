from django.contrib import admin
from .models import Checkout, CheckoutItem


# Register your models here.

class CheckoutItemInline(admin.TabularInline):
    model = CheckoutItem
    # raw_id_fields = ['product', 'checkout']


class CheckoutAdmin(admin.ModelAdmin):
    list_display = ['id', 'facilitator', 'checkout_date', 'updated', 'check_in_complete']
    list_filter = ['facilitator', 'checkout_date', 'updated', 'check_in_complete']
    # raw_id_fields = ['facilitator', ]
    inlines = [CheckoutItemInline]


admin.site.register(Checkout, CheckoutAdmin)
