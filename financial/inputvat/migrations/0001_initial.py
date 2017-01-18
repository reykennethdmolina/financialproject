# -*- coding: utf-8 -*-
# Generated by Django 1.9.10 on 2017-01-16 07:20
from __future__ import unicode_literals

import datetime
from django.conf import settings
import django.core.validators
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('chartofaccount', '0025_auto_20170116_1520'),
        ('inputvattype', '0010_auto_20170116_1520'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Inputvat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('code', models.CharField(max_length=10, unique=True)),
                ('description', models.CharField(max_length=250)),
                ('title', models.CharField(blank=True, max_length=50, null=True)),
                ('status', models.CharField(choices=[('A', 'Active'), ('I', 'Inactive'), ('C', 'Cancelled'), ('O', 'Posted'), ('P', 'Printed')], default='A', max_length=1)),
                ('enterdate', models.DateTimeField(auto_now_add=True)),
                ('modifydate', models.DateTimeField(default=datetime.datetime(2017, 1, 16, 15, 20, 22, 874000))),
                ('isdeleted', models.IntegerField(default=0)),
                ('enterby', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='inputvat_enter', to=settings.AUTH_USER_MODEL)),
                ('inputvatchartofaccount', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='chartofaccount_inputvat_id', to='chartofaccount.Chartofaccount', validators=[django.core.validators.MinValueValidator(1)])),
                ('inputvattype', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='inputvattype_id', to='inputvattype.Inputvattype', validators=[django.core.validators.MinValueValidator(1)])),
                ('modifyby', models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='inputvat_modify', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['-pk'],
                'db_table': 'inputvat',
                'permissions': (('view_inputvat', 'Can view inputvat'),),
            },
        ),
    ]
