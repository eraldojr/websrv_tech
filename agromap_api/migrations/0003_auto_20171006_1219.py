# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2017-10-06 15:19
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('agromap_api', '0002_event_kind'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='id',
            field=models.CharField(max_length=255),
        ),
    ]
