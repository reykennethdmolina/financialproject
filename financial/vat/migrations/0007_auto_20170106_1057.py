# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-01-06 02:57
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vat', '0006_auto_20170104_1636'),
    ]

    operations = [
        migrations.AlterField(
            model_name='vat',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 6, 10, 57, 54, 381000)),
        ),
    ]
