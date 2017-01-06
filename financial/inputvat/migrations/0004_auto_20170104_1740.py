# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-01-04 09:40
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inputvat', '0003_auto_20170104_1734'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inputvat',
            name='inputvattype',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='inputvattype_id', to='inputvattype.Inputvattype'),
        ),
        migrations.AlterField(
            model_name='inputvat',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 4, 17, 40, 45, 9000)),
        ),
    ]
