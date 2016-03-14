from django.conf.urls   import url
from .                  import views
urlpatterns = [
         url(r'^$',                      views.my_third_bootstrap,   name='dashboard'     ),
         url(r'^(?i)charts/$',           views.mychartsview,         name=  'charts'      ),
         url(r'^(?i)blankpage/$',        views.myblankpagesview,     name=  'blankpages'  ),
         url(r'^(?i)elements/$',         views.myelementsview,       name=  'elements'    ),
         url(r'^(?i)grid/$',             views.mygridview,           name=  'grid'        ),
         url(r'^(?i)forms/$',            views.myformsview,          name=  'forms'       ),
         url(r'^(?i)rtl/$',              views.myrtlview,            name=  'rtl'         ),
         url(r'^(?i)tables/$',           views.mytablesview,         name=  'tables'      ),
         ]

