# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2018-06-26 20:39
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('belt_2_app', '0002_trip'),
    ]

    operations = [
        migrations.AddField(
            model_name='trip',
            name='attendee',
            field=models.ManyToManyField(related_name='trips_attending', to='belt_2_app.User'),
        ),
    ]