# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-01-19 01:28
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vat', '0003_auto_20170118_1726'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vat',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 19, 9, 28, 3, 471000)),
        ),
    ]
