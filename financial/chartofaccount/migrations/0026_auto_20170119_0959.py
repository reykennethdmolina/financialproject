# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-01-19 01:59
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chartofaccount', '0025_auto_20170116_1520'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chartofaccount',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 19, 9, 59, 42, 739000)),
        ),
    ]