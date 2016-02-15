# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-12 02:57
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_auto_20160212_1049'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='date',
            field=models.DateTimeField(blank=True, default=datetime.datetime(2016, 5, 3, 0, 0), null=True),
        ),
        migrations.AlterField(
            model_name='session',
            name='details',
            field=models.TextField(blank=True, default=None, null=True),
        ),
    ]
