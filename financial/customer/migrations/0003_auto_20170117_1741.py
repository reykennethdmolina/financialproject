# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-01-17 09:41
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0002_auto_20170113_1044'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customer',
            name='creditstatus',
            field=models.CharField(blank=True, choices=[('Y', 'Yes'), ('B', 'Bad'), ('A', 'Auto-CF')], max_length=1, null=True),
        ),
        migrations.AlterField(
            model_name='customer',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 17, 17, 41, 52, 846000)),
        ),
    ]
