# -*- coding: utf-8 -*-
# Generated by Django 1.10.3 on 2016-11-30 16:41
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('payments', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='PlanPrice',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('slug', models.CharField(max_length=100)),
                ('price', models.IntegerField()),
            ],
        ),
    ]
