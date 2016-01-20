from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^(?i)equity/amanda/$',                        views.my_second_bootstrap,  name='hello'    ),
    url(r'^(?i)equity/amanda/contacts/$',               views.mycontactview,        name='contact'  ),
    url(r'^(?i)equity/amanda/htha/$',                   views.myportfolio1,           name='htha'     ),
    url(r'^(?i)equity/amanda/plantmanager/$',           views.myportfolio2,           name='plantmanager'),
    url(r'^(?i)equity/amanda/hottap/$',                 views.myportfolio3,           name='hottap'     ),
    url(r'^(?i)equity/amanda/abaqus/$',                 views.myportfolio4,           name='abaqus'     ),
    url(r'^(?i)equity/amanda/corrosion/$',              views.myportfolio,            name='corrosion'     ),
]


