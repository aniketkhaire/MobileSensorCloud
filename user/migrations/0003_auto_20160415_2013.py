# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-04-15 20:13
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_usersensordata'),
    ]

    operations = [
        migrations.AlterField(
            model_name='usersensordata',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.UserDetails'),
        ),
    ]
