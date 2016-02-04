from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^(?i)equity/hello/$',                   views.my_dashboard,         name='dashboard'    ),
    url(r'^(?i)equity/hello/template/$',          views.my_template,          name='template'     ),
    url(r'^(?i)equity/hello/icons/$',             views.my_icons,             name='icons'        ),
    url(r'^(?i)equity/hello/maps/$',              views.my_maps,              name='maps'         ),
    url(r'^(?i)equity/hello/notifications/$',     views.my_notifications,     name='notifications'),
    url(r'^(?i)equity/hello/table/$',             views.my_table,             name='table'        ),
    url(r'^(?i)equity/hello/typography/$',        views.my_typography,        name='typography'   ),
    url(r'^(?i)equity/hello/upgrade/$',           views.my_upgrade,           name='upgrade'      ),
    url(r'^(?i)equity/hello/user/$',              views.my_user,              name='user'         ),
    ]
