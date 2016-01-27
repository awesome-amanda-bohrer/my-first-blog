from django.conf.urls import include, url
from . import views

urlpatterns = [
         url(r'^(?i)equity/bohrer/$',                  views.my_third_bootstrap,   name=  'Hi'          ),
         url(r'^(?i)equity/bohrer/charts/$',           views.mychartsview,         name=  'charts'      ),
         url(r'^(?i)equity/bohrer/blankpage/$',        views.myblankpagesview,     name=  'blankpages'  ),
         url(r'^(?i)equity/bohrer/elements/$',         views.myelementsview,       name=  'elements'    ),
         url(r'^(?i)equity/bohrer/grid/$',             views.mygridview,           name=  'grid'        ),
         url(r'^(?i)equity/bohrer/forms/$',            views.myformsview,          name=  'forms'       ),
         url(r'^(?i)equity/bohrer/rtl/$',              views.myrtlview,            name=  'rtl'         ),
         url(r'^(?i)equity/bohrer/tables/$',           views.mytablesview,         name=  'tables'      ),
         ]

