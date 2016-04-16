from django.conf.urls import url
from . import views

app_name = 'sensor_admin'

urlpatterns = [

    url(r'^$', views.sensorAdmin, name='sensor_admin'),
]
