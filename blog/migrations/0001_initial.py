# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-02-12 02:18
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion
import django.utils.timezone


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Floor',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(default='SOME STRING')),
            ],
        ),
        migrations.CreateModel(
            name='Location',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(default='SOME STRING')),
                ('floor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Floor')),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('details', models.TextField()),
                ('created_date', models.DateTimeField(default=django.utils.timezone.now)),
                ('date', models.DateTimeField(blank=True, null=True)),
                ('floor', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Floor')),
                ('location', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Location')),
            ],
        ),
        migrations.CreateModel(
            name='Speaker',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField()),
                ('title', models.TextField()),
                ('imageUrl', models.TextField()),
                ('bio', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Timeslot',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.TextField(default='SOME STRING')),
            ],
        ),
        migrations.AddField(
            model_name='session',
            name='speaker',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Speaker'),
        ),
        migrations.AddField(
            model_name='session',
            name='timeslot',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Timeslot'),
        ),
    ]