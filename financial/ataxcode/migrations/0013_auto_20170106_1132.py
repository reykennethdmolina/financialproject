# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-01-06 03:32
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ataxcode', '0012_auto_20170104_1505'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ataxcode',
            name='description',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='ataxcode',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 6, 11, 32, 5, 299000)),
        ),
    ]