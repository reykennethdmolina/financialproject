# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-01-09 05:19
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankaccounttype', '0002_auto_20170109_1048'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankaccounttype',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 9, 13, 19, 32, 376000)),
        ),
    ]
