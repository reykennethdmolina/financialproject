# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-01-04 08:14
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vat', '0004_auto_20170104_1533'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vat',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 4, 16, 14, 46, 157000)),
        ),
    ]
