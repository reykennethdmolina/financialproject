# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-01-04 01:27
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('ataxcode', '0004_auto_20170104_0925'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ataxcode',
            name='enterby',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='ataxcode_enter', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='ataxcode',
            name='isdeleted',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='ataxcode',
            name='modifyby',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='ataxcode_modify', to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='ataxcode',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 4, 9, 27, 21, 121000)),
        ),
    ]