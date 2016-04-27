from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^account/login/$', 'django.contrib.auth.views.login', name='login'),
    url(r'^account/logout/$', 'django.contrib.auth.views.logout', name='logout'),
    url(r'^account/logout-then-login/$', 'django.contrib.auth.views.logout_then_login', name='logout_then_login'),
    url(r'^account/$', views.dashboard, name='dashboard'),
    url(r'^beneficiaries/$', views.beneficiary_list, name="beneficiary_list"),
    url(r'^beneficiary/(?P<id>[0-9])/$', views.beneficiary_detail, name="beneficiary_detail"),
    url(r'^tutors/$', views.tutor_list, name="tutor_list"),
    url(r'^facilitators/$', views.facilitator_list, name="facilitator_list"),
    url(r'^enumerators/$', views.enumerator_list, name="enumerator_list"),
    url(r'^centers/$', views.center_list, name="center_list"),
    url(r'^lgas/$', views.lga_list, name="lga_list"),
    url(r'^neighborhoods/$', views.neighborhood_list, name="neighborhood_list"),
    url(r'^venues/$', views.venue_list, name="venue_list"),
    url(r'^Tutorial_types/$', views.tutorialType_list, name="tutorialType_list"),
    url(r'^Equipments/$', views.equipment_list, name="equipment_list"),
]