from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^(?i)equity/amanda/$',            views.my_second_bootstrap,  name='hello'    ),
    url(r'^(?i)equity/amanda/contacts/$',   views.mycontactview,        name='contact'  ),
    url(r'^(?i)equity/amanda/html/$',       views.portfolio1,           name='htha'     ),
]

