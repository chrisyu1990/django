# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-12 02:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_remove_location_floor'),
    ]

    operations = [
        migrations.AddField(
            model_name='location',
            name='floor',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='blog.Floor'),
        ),
    ]
