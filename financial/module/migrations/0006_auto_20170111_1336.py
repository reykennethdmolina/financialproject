# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-01-11 05:36
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('module', '0005_auto_20170111_0956'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module',
            name='code',
            field=models.CharField(max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='module',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 11, 13, 36, 31, 356000)),
        ),
    ]
