# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-01-04 00:07
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vat', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vat',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 4, 8, 7, 40, 584000)),
        ),
    ]
