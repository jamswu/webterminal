# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2018-06-21 13:26
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('common', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='CommandLog',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('datetime', models.DateTimeField(auto_now=True, verbose_name='date time')),
                ('cmd', models.CharField(max_length=255, verbose_name='command')),
                ('log', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='common.Log', verbose_name='Log')),
            ],
        ),
    ]
