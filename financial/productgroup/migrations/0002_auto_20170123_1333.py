# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-01-23 05:33
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('productgroup', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='productgroup',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 23, 13, 33, 2, 260000)),
        ),
    ]
