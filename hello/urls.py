from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^(?i)equity/hello/$',                   views.my_dashboard,      name='dashboard'    ),
    url(r'^(?i)equity/hello/template/$',          views.template,          name='template'     ),
    url(r'^(?i)equity/hello/icons/$',             views.icons,             name='icons'        ),
    url(r'^(?i)equity/hello/maps/$',              views.maps,              name='maps'         ),
    url(r'^(?i)equity/hello/notifications/$',     views.notifications,     name='notifications'),
    url(r'^(?i)equity/hello/table/$',             views.table,             name='table'        ),
    url(r'^(?i)equity/hello/typography/$',        views.typography,        name='typography'   ),
    url(r'^(?i)equity/hello/upgrade/$',           views.upgrade,           name='upgrade'      ),
    url(r'^(?i)equity/hello/user/$',              views.user,              name='user'         ),
    ]
