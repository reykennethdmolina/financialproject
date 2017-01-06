# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-01-04 03:45
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('bank', '0002_auto_20161216_1536'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bank',
            name='isdeleted',
            field=models.IntegerField(default=0, max_length=1),
        ),
        migrations.AlterField(
            model_name='bank',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 4, 11, 45, 4, 319691)),
        ),
        migrations.AlterField(
            model_name='bank',
            name='status',
            field=models.CharField(choices=[('A', 'Active'), ('C', 'Cancelled'), ('O', 'Posted'), ('P', 'Printed')], default='A', max_length=1),
        ),
    ]