# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-01-18 09:26
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bankaccount', '0002_auto_20170118_1725'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bankaccount',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 18, 17, 26, 16, 811000)),
        ),
    ]