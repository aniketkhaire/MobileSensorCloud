from django.conf.urls import url
from . import views

app_name = 'monitor'

urlpatterns = [

    url(r'^monitor$', views.ShowMonitorView.as_view(), name='monitor'),
    #url(r'^(?P<pk>[0-9]+)/$', views.sensorDataView, name='sensor-data'),
]
