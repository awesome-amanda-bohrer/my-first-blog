from django.conf.urls import include, url
from . import views

urlpatterns = [
         url(r'^(?i)equity/personal/$',        views.my_bootstrap,   name=  'ok'),
         ]


