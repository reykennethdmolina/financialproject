# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-01-10 09:03
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wtax', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='wtax',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 10, 17, 3, 16, 983000)),
        ),
    ]
