from django.conf.urls   import url
from .                  import views

urlpatterns = [
    url(r'^$',                      views.my_dashboard1,           name='dashboard'    ),
    url(r'^(?i)template/$',         views.my_template1,            name='template'     ),
    url(r'^(?i)buttons/$',          views.my_buttons1,             name='buttons'      ),
    url(r'^(?i)calendar/$',         views.my_calendar1,            name='calendar'     ),
    url(r'^(?i)charts/$',           views.my_charts1,              name='charts'       ),
    url(r'^(?i)datatable/$',        views.my_datatable1,           name='datatable'    ),
    url(r'^(?i)elements/$',         views.my_elements1,            name='elements'     ),
    url(r'^(?i)extended/$',         views.my_extended1,            name='extended'     ),
    url(r'^(?i)fullscreen/$',       views.my_fullscreen1,          name='fullscreen'   ),
    url(r'^(?i)google/$',           views.my_google1,              name='google'       ),
    url(r'^(?i)grid/$',             views.my_grid1,                name='grid'         ),
    url(r'^(?i)icons/$',            views.my_icons1,               name='icons'        ),
    url(r'^(?i)lock/$',             views.my_lock1,                name='lock'         ),
    url(r'^(?i)login/$',            views.my_login1,               name='login'        ),
    url(r'^(?i)notifications/$',    views.my_notifications1,       name='notifications'),
    url(r'^(?i)panels/$',           views.my_panels1,              name='panels'       ),
    url(r'^(?i)plainpage/$',        views.my_plainpage1,           name='plainpage'    ),
    url(r'^(?i)register/$',         views.my_register1,            name='register'     ),
    url(r'^(?i)sweetalert/$',       views.my_sweetalert1,          name='sweetalert'   ),
    url(r'^(?i)typography/$',       views.my_typography1,          name='typography'   ),
    url(r'^(?i)user/$',             views.my_user1,                name='user'         ),
    url(r'^(?i)validation/$',       views.my_validation1,          name='validation'   ),
    url(r'^(?i)vector/$',           views.my_vector1,              name='vector'       ),
    url(r'^(?i)wizard/$',           views.my_wizard1,              name='wizard'       ),
    url(r'^(?i)regular/$',          views.my_regular1,             name='regular'      ),
    url(r'^(?i)regulartable/$',     views.my_regular2,             name='regulartable' ),
    url(r'^(?i)extendedtable/$',    views.my_extended4,            name='extended'     ),
    ]

