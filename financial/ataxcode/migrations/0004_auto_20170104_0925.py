# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-01-04 01:25
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ataxcode', '0003_auto_20170104_0923'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ataxcode',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 4, 9, 25, 49, 313000)),
        ),
    ]
