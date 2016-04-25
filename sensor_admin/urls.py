from django.conf.urls import url
from . import views

app_name = 'sensor_admin'

urlpatterns = [

    url(r'^overview$', views.sensorAdmin, name='sensor_admin'),
    url(r'^manage_sensors$', views.manageAvailableSensors, name='admin_manage_sensors'),
    url(r'^manage_users$', views.manageAvailableUsers, name='manage_users'),
]
