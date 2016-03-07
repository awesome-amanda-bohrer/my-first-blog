from django.conf.urls   import url
from .                  import views

urlpatterns = [
    url(r'^$',                      views.my_dashboard2,           name='dashboard'    ),
    url(r'^(?i)template/$',         views.my_template2,            name='template'     ),
    url(r'^(?i)buttons/$',          views.my_buttons2,             name='buttons'      ),
    url(r'^(?i)calendar/$',         views.my_calendar2,            name='calendar'     ),
    url(r'^(?i)charts/$',           views.my_charts2,              name='charts'       ),
    url(r'^(?i)datatable/$',        views.my_datatable2,           name='datatable'    ),
    url(r'^(?i)elements/$',         views.my_elements2,            name='elements'     ),
    url(r'^(?i)extended/$',         views.my_extended2,            name='extended'     ),
    url(r'^(?i)fullscreen/$',       views.my_fullscreen2,          name='fullscreen'   ),
    url(r'^(?i)google/$',           views.my_google2,              name='google'       ),
    url(r'^(?i)grid/$',             views.my_grid2,                name='grid'         ),
    url(r'^(?i)icons/$',            views.my_icons2,               name='icons'        ),
    url(r'^(?i)lock/$',             views.my_lock2,                name='lock'         ),
    url(r'^(?i)login/$',            views.my_login2,               name='login'        ),
    url(r'^(?i)notifications/$',    views.my_notifications2,       name='notifications'),
    url(r'^(?i)panels/$',           views.my_panels2,              name='panels'       ),
    url(r'^(?i)plainpage/$',        views.my_plainpage2,           name='plainpage'    ),
    url(r'^(?i)register/$',         views.my_register2,            name='register'     ),
    url(r'^(?i)sweetalert/$',       views.my_sweetalert2,          name='sweetalert'   ),
    url(r'^(?i)typography/$',       views.my_typography2,          name='typography'   ),
    url(r'^(?i)user/$',             views.my_user2,                name='user'         ),
    url(r'^(?i)validation/$',       views.my_validation2,          name='validation'   ),
    url(r'^(?i)vector/$',           views.my_vector2,              name='vector'       ),
    url(r'^(?i)wizard/$',           views.my_wizard2,              name='wizard'       ),
    url(r'^(?i)regular/$',          views.my_regular3,             name='regular'      ),
    url(r'^(?i)regulartable/$',     views.my_regular4,             name='regulartable' ),
    url(r'^(?i)extendedtable/$',    views.my_extended3,            name='extended'     ),
    ]


