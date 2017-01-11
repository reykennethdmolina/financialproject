# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-01-11 05:41
from __future__ import unicode_literals

import datetime
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('module', '0006_auto_20170111_1336'),
    ]

    operations = [
        migrations.AlterField(
            model_name='module',
            name='django_content_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='django_content_type_id', to='contenttypes.ContentType', validators=[django.core.validators.MinValueValidator(1)]),
        ),
        migrations.AlterField(
            model_name='module',
            name='modifydate',
            field=models.DateTimeField(default=datetime.datetime(2017, 1, 11, 13, 41, 23, 833000)),
        ),
    ]