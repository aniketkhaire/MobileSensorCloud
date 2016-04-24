from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from sensor_owner.models import SensorDetail

# Create your models here.


class UserDetail(models.Model):
    user_name = models.CharField(max_length=100)
    user_role = models.CharField(max_length=30)
    name = models.CharField(max_length=100)
    email = models.EmailField()

    def __str__(self):
        return self.user_name


class UserRole(models.Model):
    role = models.CharField(max_length=30)
    description = models.CharField(max_length=200)

    def __str__(self):
        return self.role


class UserSensorDetail(models.Model):
    user_name = models.ForeignKey(User, on_delete=models.CASCADE)
    sensor_id = models.ForeignKey(SensorDetail, on_delete=models.CASCADE)
