# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-01-16 07:01
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inputvattype', '0003_auto_20170110_1703'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inputvattype',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 16, 15, 1, 13, 571000)),
        ),
    ]
