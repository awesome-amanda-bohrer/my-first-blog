from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^(?i)equity/amanda/$',   views.my_second_bootstrap,  name='hello' ),
]

