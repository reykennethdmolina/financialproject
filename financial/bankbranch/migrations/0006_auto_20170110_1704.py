# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-01-10 09:04
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankbranch', '0005_auto_20170109_1029'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='bankbranch',
            options={'ordering': ['-pk'], 'permissions': (('view_bankbranch', 'Can view bankbranch'),)},
        ),
        migrations.AlterField(
            model_name='bankbranch',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 10, 17, 4, 23, 679000)),
        ),
    ]
