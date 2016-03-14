from django.conf.urls   import url
from .                  import views

urlpatterns = [
    url(r'^$',                      views.my_index,                 name='dashboard'    ),
    url(r'^(?i)indexrtl/$',         views.my_indexrtl,              name='indexrtl'     ),
    url(r'^(?i)blankpage/$',        views.my_blankpage,             name='blankpage'    ),
  ]
