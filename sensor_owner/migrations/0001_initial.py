# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-15 04:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='SensorDetails',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('station', models.CharField(max_length=400)),
                ('station_desc', models.CharField(max_length=800)),
                ('sensor_type', models.CharField(max_length=100)),
                ('latitude', models.FloatField(max_length=10)),
                ('longitude', models.FloatField(max_length=10)),
                ('url', models.CharField(max_length=800)),
                ('sensorOwner', models.CharField(max_length=200)),
            ],
        ),
    ]
