from django.contrib import admin
from .models import Beneficiary


class BeneficiaryAdmin(admin.ModelAdmin):
    """These are the fields that will be displayed on the Beneficiary page"""
    list_display = ('beneficiary_id', 'first_name', 'last_name', 'beneficiary_age', 'is_in_school', 'gender')
    search_fields = ('beneficiary_id', 'first_name', 'last_name') #display a search field from which these fileds could be searched
    fields = (
        'beneficiary_id',
        'first_name',
        'last_name',
        'gender',
        'year_of_birth',
        'is_in_school'
    )

admin.site.register(Beneficiary, BeneficiaryAdmin)

