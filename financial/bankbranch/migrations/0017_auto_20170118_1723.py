# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-01-18 09:23
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankbranch', '0016_auto_20170112_0945'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankbranch',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 18, 17, 23, 56, 886000)),
        ),
    ]
