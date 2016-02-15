# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-12 03:20
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_auto_20160212_1101'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='session',
            name='speaker',
        ),
        migrations.AddField(
            model_name='session',
            name='speaker',
            field=models.ManyToManyField(to='blog.Speaker'),
        ),
    ]