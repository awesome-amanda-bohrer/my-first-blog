from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^(?i)equity/amanda/$',                        views.my_second_bootstrap,  name='hello'    ),
    url(r'^(?i)equity/amanda/contacts/$',               views.mycontactview,        name='contact'  ),
    url(r'^(?i)equity/amanda/htha/$',                   views.myportfolio1,         name='htha'     ),
    url(r'^(?i)equity/amanda/cokedrums/$',              views.myblog1,              name='cokedrums'),
    url(r'^(?i)equity/amanda/404/$',                    views.my404,                name='404'      ),
    ]


