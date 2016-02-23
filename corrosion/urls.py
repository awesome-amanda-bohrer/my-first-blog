from django.conf.urls   import url
from .                  import views

urlpatterns = [
    url(r'^$',                      views.my_dashboard3,           name='dashboard'    ),
    url(r'^(?i)template/$',         views.my_template3,            name='template'     ),
    url(r'^(?i)buttons/$',          views.my_buttons3,             name='buttons'      ),
    url(r'^(?i)calendar/$',         views.my_calendar3,            name='calendar'     ),
    url(r'^(?i)charts/$',           views.my_charts3,              name='charts'       ),
    url(r'^(?i)datatable/$',        views.my_datatable3,           name='datatable'    ),
    url(r'^(?i)elements/$',         views.my_elements3,            name='elements'     ),
    url(r'^(?i)extended/$',         views.my_extended3,            name='extended'     ),
    url(r'^(?i)fullscreen/$',       views.my_fullscreen3,          name='fullscreen'   ),
    url(r'^(?i)google/$',           views.my_google3,              name='google'       ),
    url(r'^(?i)grid/$',             views.my_grid3,                name='grid'         ),
    url(r'^(?i)icons/$',            views.my_icons3,               name='icons'        ),
    url(r'^(?i)lock/$',             views.my_lock3,                name='lock'         ),
    url(r'^(?i)login/$',            views.my_login3,               name='login'        ),
    url(r'^(?i)notifications/$',    views.my_notifications3,       name='notifications'),
    url(r'^(?i)panels/$',           views.my_panels3,              name='panels'       ),
    url(r'^(?i)plainpage/$',        views.my_plainpage3,           name='plainpage'    ),
    url(r'^(?i)register/$',         views.my_register3,            name='register'     ),
    url(r'^(?i)sweetalert/$',       views.my_sweetalert3,          name='sweetalert'   ),
    url(r'^(?i)typography/$',       views.my_typography3,          name='typography'   ),
    url(r'^(?i)user/$',             views.my_user3,                name='user'         ),
    url(r'^(?i)validation/$',       views.my_validation3,          name='validation'   ),
    url(r'^(?i)vector/$',           views.my_vector3,              name='vector'       ),
    url(r'^(?i)wizard/$',           views.my_wizard3,              name='wizard'       ),
    url(r'^(?i)regular/$',          views.my_regular5,             name='regular'      ),
    url(r'^(?i)regulartable/$',     views.my_regular6,             name='regulartable' ),
    ]



