from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserDetails(models.Model):
    user_name = models.CharField(max_length=100)
    user_role = models.CharField(max_length=30)
    name = models.CharField(max_length=100)
    email = models.EmailField()

class UserRoles(models.Model):
    role = models.CharField(max_length=30)
    description = models.CharField(max_length=200)

class LoginCredentials(models.Model):
    user_detail = models.ForeignKey(UserDetails, on_delete=models.CASCADE)
    user_role = models.ForeignKey(UserRoles, on_delete=models.CASCADE)
    password = models.CharField(max_length=50)

class SensorTypes(models.Model):
    sensor_id = models.CharField(max_length=400)
    type = models.CharField(max_length=200)
    description = models.CharField(max_length=400)
    unit = models.CharField(max_length=50)

class UserSensorData(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    sensor_name = models.CharField(max_length=200)
    sensor_location = models.CharField(max_length=200)
    sensor_type = models.CharField(max_length=200)
    sensor_provider = models.CharField(max_length=200)
    sensor_status = models.BooleanField()

    def __str__(self):
        return self.sensor_name
