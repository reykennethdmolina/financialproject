# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-01-10 09:04
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('mainmodule', '0002_auto_20170109_1416'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='mainmodule',
            options={'ordering': ['-pk'], 'permissions': (('view_mainmodule', 'Can view mainmodule'),)},
        ),
        migrations.AlterField(
            model_name='mainmodule',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 10, 17, 4, 40, 183000)),
        ),
    ]
