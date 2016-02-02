from django.conf.urls import include, url
from . import views

urlpatterns = [
         url(r'^(?i)equity/webapp/$',        views.my_fourth_bootstrap,   name=  'Amanda'),
         ]
