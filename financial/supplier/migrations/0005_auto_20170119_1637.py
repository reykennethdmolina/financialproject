# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-01-19 08:37
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('supplier', '0004_auto_20170119_1634'),
    ]

    operations = [
        migrations.AlterField(
            model_name='supplier',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 19, 16, 37, 12, 152000)),
        ),
    ]
