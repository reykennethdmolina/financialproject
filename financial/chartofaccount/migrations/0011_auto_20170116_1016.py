# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-01-16 02:16
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('chartofaccount', '0010_auto_20170116_1012'),
    ]

    operations = [
        migrations.AlterField(
            model_name='chartofaccount',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 16, 10, 16, 16, 701000)),
        ),
    ]
