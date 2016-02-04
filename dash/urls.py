from django.conf.urls import include, url
from . import views

urlpatterns = [
         url(r'^(?i)dash/$',        views.my_dashboard,   name=  'amanda'),
         ]


