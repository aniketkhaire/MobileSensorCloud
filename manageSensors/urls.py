from django.conf.urls import url
from . import views

app_name = 'manageSensors'

urlpatterns = [

    url(r'^manageSensors$', views.manageSensors, name='manageSensors'),
    url(r'^manageSensors/(?P<pk>[0-9]+)/$', views.addSensor, name="addSensor"),
    url(r'^manageSensors/(?P<pk>[0-9]+)/delete$', views.deleteSensor, name="deleteSensor"),
    #url(r'^(?P<pk>[0-9]+)/$', views.sensorDataView, name='sensor-data'),
]
