# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-07 07:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0016_auto_20160107_0635'),
    ]

    operations = [
        migrations.AddField(
            model_name='namedentity',
            name='pref_label_slug',
            field=models.SlugField(blank=True, null=True, verbose_name='Entity PrefLabel Slug'),
        ),
    ]
