from django.conf.urls import url
from . import views

app_name = 'manage_sensors'

urlpatterns = [

    url(r'^manage_sensors$', views.manage_sensors, name='manage_sensors'),
    url(r'^manage_sensors/(?P<pk>[0-9]+)/$', views.add_sensor, name="add_sensor"),
    url(r'^manage_sensors/(?P<pk>[0-9]+)/delete/$', views.delete_sensor, name="delete_sensor"),
]
