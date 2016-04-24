from django.conf.urls import url
from . import views

app_name = 'sensor_owner'

urlpatterns = [
    url(r'^overview$', views.ShowSensorsView.as_view(), name='owner_dashboard'),
    url(r'^manage$', views.AddSensorView.as_view(), name='owner_manage'),
]
