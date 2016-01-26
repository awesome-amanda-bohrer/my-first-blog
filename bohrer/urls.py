from django.conf.urls import include, url
from . import views

urlpatterns = [
         url(r'^(?i)equity/bohrer/$',       views.my_third_bootstrap,   name=  'Hi'),
         ]

