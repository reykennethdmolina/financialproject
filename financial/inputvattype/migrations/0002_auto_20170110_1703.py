# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-01-10 09:03
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('inputvattype', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='inputvattype',
            options={'ordering': ['-pk'], 'permissions': (('view_inputvattype', 'Can view inputvattype'),)},
        ),
        migrations.AlterField(
            model_name='inputvattype',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 10, 17, 3, 4, 658000)),
        ),
    ]
