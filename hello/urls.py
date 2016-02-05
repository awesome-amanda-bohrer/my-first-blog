from django.conf.urls   import url
from .                  import views

urlpatterns = [
    url(r'^$',                      views.my_dashboard,         name='dashboard'    ),
    url(r'^(?i)template/$',         views.my_template,          name='template'     ),
    url(r'^(?i)icons/$',            views.my_icons,             name='icons'        ),
    url(r'^(?i)maps/$',             views.my_maps,              name='maps'         ),
    url(r'^(?i)notifications/$',    views.my_notifications,     name='notifications'),
    url(r'^(?i)table/$',            views.my_table,             name='table'        ),
    url(r'^(?i)typography/$',       views.my_typography,        name='typography'   ),
    url(r'^(?i)upgrade/$',          views.my_upgrade,           name='upgrade'      ),
    url(r'^(?i)user/$',             views.my_user,              name='user'         ),
    ]
