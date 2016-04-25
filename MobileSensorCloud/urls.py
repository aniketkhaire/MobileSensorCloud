from django.conf.urls import include, url
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^user/', include('user.urls')),
    url(r'^user/', include('dashboard.urls')),
    url(r'^user/', include('monitor.urls')),
    url(r'^user/', include('manage_sensors.urls')),
    url(r'^sensor_owner/', include('sensor_owner.urls')),
    url(r'^sensor_admin/', include('sensor_admin.urls')),
    url(r'^chaining/', include('smart_selects.urls')),
]

urlpatterns += staticfiles_urlpatterns()
