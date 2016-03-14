"""DjangoGirl URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.9/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url
from django.contrib import admin
from django.conf.urls import include
urlpatterns = [
    url(r'^boot/'            ,   include(admin.site.urls))      ,
    url(r'^hottap/'          ,   include('hottap.urls'))        ,
    url(r'^fatigue_test/'    ,   include('fatigue_test.urls'))  ,
    url(r'^corrosion/'       ,   include('corrosion.urls'))     ,
    url(r'^fatigue/'         ,   include('fatigue.urls'))       ,
    url(r'^custom/'          ,   include('custom.urls'))        ,
]

