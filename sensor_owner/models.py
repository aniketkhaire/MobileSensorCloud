from __future__ import unicode_literals
from django.db import models
from django.contrib.auth.models import User
from smart_selects.db_fields import ChainedForeignKey

# Create your models here.


class SensorType(models.Model):
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name;


class SensorUnit(models.Model):
    sensor_type = models.ForeignKey(SensorType)
    name = models.CharField(max_length=255)

    def __str__(self):
        return self.name;


class SensorDetail(models.Model):
    sensor_id = models.CharField(max_length=100)
    station_name = models.CharField(max_length=400)
    station_desc = models.CharField(max_length=800)
    sensor_type = models.ForeignKey(SensorType)
    sensor_unit = ChainedForeignKey(
        SensorUnit,
        chained_field="sensor_type",
        chained_model_field="sensor_type",
        show_all=False,
        auto_choose=True
    )

    latitude = models.FloatField(max_length=10)
    longitude = models.FloatField(max_length=10)
    location = models.CharField(max_length=400)
    url = models.CharField(max_length=800)
    active = models.BooleanField(default=True)
    sensorOwner = models.ForeignKey(User, on_delete=models.CASCADE)
    ip_address = models.CharField(max_length=100, default='DEFAULT_VALUE')

    def __str__(self):
        return self.station_name+''