# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-01-16 07:02
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inputvattype', '0004_auto_20170116_1501'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inputvattype',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 16, 15, 2, 1, 356000)),
        ),
    ]
