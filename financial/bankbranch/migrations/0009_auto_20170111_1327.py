# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-01-11 05:27
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankbranch', '0008_auto_20170111_1321'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankbranch',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 11, 13, 27, 39, 344000)),
        ),
    ]