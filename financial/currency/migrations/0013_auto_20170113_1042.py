# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-01-13 02:42
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0012_auto_20170112_0945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currency',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 13, 10, 42, 45, 333000)),
        ),
    ]
