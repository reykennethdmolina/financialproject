# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-01-09 02:12
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('currency', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='currency',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 9, 10, 12, 25, 24000)),
        ),
    ]
