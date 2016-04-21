from django.contrib import admin
from django.core import urlresolvers

from .forms import BeneficiaryForm
from .models import *


class LocalGovAreaAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class VenueAdmin(admin.ModelAdmin):
    list_display = ('address','coordinate',)
    search_fields = ('address','coordinate',)


class TutorialTypeAdmin(admin.ModelAdmin):
    list_display = ('tutorial_type',)
    search_fields = ('tutorial_type',)
    list_filter = ('tutorial_type',)


class FacilitatorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'gender', 'account_number', 'email', 'phone_number',)
    fields = ['first_name', 'last_name', 'gender', 'email', 'neighborhood', 'account_number', 'phone_number']
    search_fields = ('full_name', 'first_name', 'last_name', 'account_number', 'email', 'phone_number',)
    raw_id_fields = ('neighborhood',)
    ordering = ['email']
    list_filter = ('gender',)


class CenterAdmin(admin.ModelAdmin):
    list_display = ('title', 'facilitator', 'group_size',)
    fields = ['title', 'venue', 'tutorial_types', 'facilitator', 'group_size']
    raw_id_fields = ('venue', 'facilitator',)
    search_fields = ('title',)
    filter_horizontal = ('tutorial_types',)
    ordering = ['title']


class BeneficiaryAdmin(admin.ModelAdmin):
    form = BeneficiaryForm
    list_display = ('beneficiary_id', 'full_name', 'gender', 'is_in_school', 'age', 'link_to_neigh')
    fields = ['beneficiary_id', 'first_name', 'last_name', 'gender', 'neighborhood', 'center', 'age', 'is_in_school']
    raw_id_fields = ('neighborhood', 'center',)
    ordering = ['first_name', 'last_name']
    search_fields = ('beneficiary_id', 'first_name', 'beneficiary_id',)
    list_filter = ('is_in_school', 'gender', 'age')

    # this is a test function that lets django list neighborhoods in the beneficiary table as links to those
    # neighborhoods. This allows users to intanly click and view details of each neighborhood right from the
    # list of beneficiaries

    def link_to_neigh(self, obj):
        link = urlresolvers.reverse("admin:tela_neighborhood_change", args=[obj.neighborhood.id])
        return u'<a href="%s">%s</a>' % (link, obj.neighborhood.name)

    link_to_neigh.allow_tags = True


class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('serial_num', 'equipment_type', 'status', 'created','updated', 'is_available',)
    fields = ['serial_num', 'equipment_type', 'status', 'is_available']
    search_fields = ('serial_num', 'equipment_type', 'is_available',)
    ordering = ['status', 'serial_num']
    list_filter = ('equipment_type', 'status', 'created', 'updated', 'is_available',)


class EnumeratorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'gender', 'account_number', 'neighborhood', 'email', 'phone_number',)
    fields = ['first_name', 'last_name', 'email', 'gender', 'neighborhood', 'account_number', 'phone_number']
    ordering = ['first_name', 'last_name']
    search_fields = ('first_name', 'last_name', 'email', 'phone_number',)
    list_filter = ('gender',)


class TutorAdmin(admin.ModelAdmin):
    list_display = ('tutor_id', 'full_name', 'gender', 'major', 'classification', 'email', 'phone_number')
    fields = ['tutor_id', 'first_name', 'last_name', 'gender', 'major', 'classification', 'email', 'phone_number']
    ordering = ['tutor_id', 'first_name', 'last_name', ]
    search_fields = ('tutor_id', 'first_name', 'last_name', 'email',)
    list_filter = ('gender', 'classification',)


class PreAssessmentAdmin(admin.ModelAdmin):
    list_display = ('beneficiary', 'enumerator',)
    raw_id_fields = ('beneficiary', 'enumerator',)
    search_fields = ('enumerator', 'beneficiary')
    ordering = ['beneficiary', 'enumerator']


class PostAssessmentAdmin(admin.ModelAdmin):
    list_display = ('beneficiary', 'enumerator',)
    raw_id_fields = ('beneficiary', 'enumerator',)
    search_fields = ('enumerator', 'beneficiary')
    ordering = ['beneficiary', 'enumerator']


class NeighborhoodAdmin(admin.ModelAdmin):
    list_display = ('name', 'lga')
    search_fields = ('name', 'lga')
    raw_id_fields = ('lga',)


admin.site.register(LocalGovArea, LocalGovAreaAdmin)
admin.site.register(Venue, VenueAdmin)
admin.site.register(TutorialType, TutorialTypeAdmin)
admin.site.register(Facilitator, FacilitatorAdmin)
admin.site.register(Center, CenterAdmin)
admin.site.register(Beneficiary, BeneficiaryAdmin)
admin.site.register(Equipment, EquipmentAdmin)
admin.site.register(Tutor, TutorAdmin)
admin.site.register(Enumerator, EnumeratorAdmin)
admin.site.register(PreAssessment, PreAssessmentAdmin)
admin.site.register(PostAssessment, PostAssessmentAdmin)
admin.site.register(Neighborhood, NeighborhoodAdmin)
