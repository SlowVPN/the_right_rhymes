# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-06 07:18
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0012_auto_20160106_0642'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='xref',
            options={'ordering': ['xref_word']},
        ),
    ]