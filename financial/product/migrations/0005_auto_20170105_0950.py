# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-01-05 01:50
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product', '0004_auto_20170105_0942'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='cmsgroup',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='product',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 5, 9, 50, 52, 439085)),
        ),
    ]
