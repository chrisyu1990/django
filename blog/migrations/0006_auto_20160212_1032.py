# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-12 02:32
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20160212_1031'),
    ]

    operations = [
        migrations.AlterField(
            model_name='session',
            name='details',
            field=models.TextField(),
        ),
    ]
