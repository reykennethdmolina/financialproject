# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-01-11 06:33
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0010_auto_20170111_1419'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bank',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 11, 14, 33, 57, 758000)),
        ),
    ]
