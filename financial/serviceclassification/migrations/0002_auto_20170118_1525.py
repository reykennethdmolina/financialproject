# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-01-18 07:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('serviceclassification', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviceclassification',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 18, 15, 25, 35, 419000)),
        ),
    ]