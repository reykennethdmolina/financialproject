# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-01-16 07:18
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chartofaccount', '0023_auto_20170116_1514'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chartofaccount',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 16, 15, 18, 40, 490000)),
        ),
    ]
