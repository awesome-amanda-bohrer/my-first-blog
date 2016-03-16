from django.conf.urls   import url
from .                  import views
urlpatterns = [
         url(r'^$',                      views.my_third_bootstrap,   name='dashboard'     ),
         url(r'^(?i)charts/$',           views.mychartsview,         name=  'charts'      ),
         url(r'^(?i)selection/$',        views.myselectionview,     name=  'selection'    ),
         url(r'^(?i)input/$',        views.myinputview,         name=  'input'    ),
         url(r'^(?i)elements/$',         views.myelementsview,       name=  'elements'    ),
         url(r'^(?i)grid/$',             views.mygridview,           name=  'grid'        ),
         url(r'^(?i)forms/$',            views.myformsview,          name=  'forms'       ),
         url(r'^(?i)tables/$',           views.mytablesview,         name=  'tables'      ),
         url(r'^(?i)sleeve/$',           views.mysleeveview,         name=  'sleeve'      ),
         ]
