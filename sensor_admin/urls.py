from django.conf.urls import url
from . import views

app_name = 'cloud_admin'

urlpatterns = [

    url(r'^overview$', views.sensorAdmin, name='cloud_admin'),
    url(r'^manage_sensors$', views.manageAvailableSensors, name='manage_sensors'),
    url(r'^manage_users$', views.manageAvailableUsers, name='manage_users'),
]
