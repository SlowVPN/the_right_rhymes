# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-19 18:00
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='song',
            name='slug',
            field=models.CharField(blank=True, db_index=True, max_length=1000, null=True, verbose_name='Slug'),
        ),
    ]
