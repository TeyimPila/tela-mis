from django.conf.urls import url
from . import views

urlpatterns = [
    url(r'^create/$', views.checkout_create, name='checkout_create'),
]
