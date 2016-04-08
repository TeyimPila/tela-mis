from django.contrib import admin
from .models import *


class LocalGovAreaAdmin(admin.ModelAdmin):
    list_display = ('name',)
    search_fields = ('name',)


class VenueAdmin(admin.ModelAdmin):
    list_display = ('coordinate',)


class TutorialTypeAdmin(admin.ModelAdmin):
    list_display = ('tutorial_type',)
    search_fields = ('tutorial_type',)


class FacilitatorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'gender', 'account_number', 'email', 'phone_number',)
    fields = ['first_name', 'last_name', 'gender', 'email', 'neighborhood', 'account_number', 'phone_number']
    search_fields = ('full_name', 'first_name', 'last_name', 'account_number', 'email', 'phone_number',)
    ordering = ['email']


class CenterAdmin(admin.ModelAdmin):
    list_display = ('title', 'facilitator', 'group_size',)
    fields = ['title', 'venue', 'tutorial_types', 'facilitator', 'group_size']
    raw_id_fields = ('tutorial_types', 'venue', 'facilitator',)
    search_fields = ('tutorial_types', 'title',)
    ordering = ['title']


class BeneficiaryAdmin(admin.ModelAdmin):
    list_display = ('beneficiary_id', 'full_name', 'gender', 'is_in_school', 'age', 'neighborhood')
    fields = ['beneficiary_id', 'first_name', 'last_name', 'gender', 'neighborhood', 'center', 'age', 'is_in_school']
    raw_id_fields = ('neighborhood', 'center',)
    ordering = ['first_name', 'last_name']
    search_fields = ('beneficiary_id', 'first_name', 'beneficiary_id',)


class EquipmentAdmin(admin.ModelAdmin):
    list_display = ('serial_num', 'equipment_type', 'status', 'check_in_status', 'availability',)
    fields = ['serial_num', 'equipment_type', 'facilitator', 'status', 'check_in_status', 'check_out_status',
              'availability']
    raw_id_fields = ('facilitator',)
    search_fields = ('serial_num', 'equipment_type', 'availability',)
    ordering = ['check_in_status', 'serial_num']


class EnumeratorAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'gender', 'account_number', 'neighborhood', 'email', 'phone_number',)
    fields = ['first_name', 'last_name', 'email', 'gender', 'neighborhood', 'account_number', 'phone_number']
    ordering = ['first_name', 'last_name']
    search_fields = ('first_name', 'last_name', 'email', 'phone_number',)


class TutorAdmin(admin.ModelAdmin):
    list_display = ('tutor_id', 'full_name', 'gender', 'major', 'classification', 'email', 'phone_number')
    fields = ['tutor_id', 'first_name', 'last_name', 'gender', 'major', 'classification', 'email', 'phone_number']
    ordering = ['tutor_id', 'first_name', 'last_name', ]
    search_fields = ('tutor_id', 'first_name', 'last_name', 'email',)


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
