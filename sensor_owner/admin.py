from django.contrib import admin
from sensor_owner.models import SensorDetail, SensorUnit, SensorType

# Register your models here.

admin.site.register(SensorType)
admin.site.register(SensorUnit)
admin.site.register(SensorDetail)