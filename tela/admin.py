from django.contrib import admin
from .models import *

# register models here


class VenueAdmin(admin.ModelAdmin):
    list_display = ('address', 'coordinate')


class CenterAdmin(admin.ModelAdmin):
    list_display = ('title', 'group_size')
    # the order in which fields will appear in the model form
    fields = ['title', 'group_size', 'venue', 'tutorial_types', 'facilitator']
    filter_horizontal = ('tutorial_types',)


class BeneficiaryAdmin(admin.ModelAdmin):
    list_display = ('beneficiary_id', 'first_name', 'last_name', 'gender', 'lga', 'age', 'is_in_school', 'center')

admin.site.register(Beneficiary, BeneficiaryAdmin)
admin.site.register(Enumerator)
admin.site.register(Facilitator)
admin.site.register(LocalGovArea)
admin.site.register(Equipment)
admin.site.register(Tutor)
admin.site.register(PreAssessment)
admin.site.register(PostAssessment)
admin.site.register(Center, CenterAdmin)
admin.site.register(TutorialType)
admin.site.register(Venue, VenueAdmin)

