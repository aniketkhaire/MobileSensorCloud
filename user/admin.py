from django.contrib import admin
from .models import UserRole, UserDetail, UserSensorDetail
# Register your models here.

admin.site.register(UserRole)
admin.site.register(UserDetail)
admin.site.register(UserSensorDetail)