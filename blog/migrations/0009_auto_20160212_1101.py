# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-12 03:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_auto_20160212_1057'),
    ]

    operations = [
        migrations.AlterField(
            model_name='beacon',
            name='major',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='beacon',
            name='minor',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='floor',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='location',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='name',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='speaker',
            name='title',
            field=models.CharField(max_length=200),
        ),
        migrations.AlterField(
            model_name='timeslot',
            name='name',
            field=models.CharField(max_length=200),
        ),
    ]
