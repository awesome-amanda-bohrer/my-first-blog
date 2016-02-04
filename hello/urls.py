from django.conf.urls import include, url
from . import views

urlpatterns = [
    url(r'^(?i)hello/$',                   views.my_dashboard,      name='hello'        ),
    url(r'^(?i)hello/template/$',          views.template,          name='template'     ),
    url(r'^(?i)hello/icons/$',             views.icons,             name='icons'        ),
    url(r'^(?i)hello/maps/$',              views.maps,              name='maps'         ),
    url(r'^(?i)hello/notifications/$',     views.notifications,     name='notifications'),
    url(r'^(?i)hello/table/$',             views.table,             name='table'        ),
    url(r'^(?i)hello/typography/$',        views.typography,        name='typography'   ),
    url(r'^(?i)hello/upgrade/$',           views.upgrade,           name='upgrade'      ),
    url(r'^(?i)hello/user/$',              views.user,              name='user'         ),
    ]
