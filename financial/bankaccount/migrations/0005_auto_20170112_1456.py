# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-01-12 06:56
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankaccount', '0004_merge'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankaccount',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 12, 14, 56, 26, 267000)),
        ),
    ]
