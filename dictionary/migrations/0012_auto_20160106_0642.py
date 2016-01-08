# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2016-01-06 06:42
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0011_xref'),
    ]

    operations = [
        migrations.AddField(
            model_name='sense',
            name='xrefs',
            field=models.ManyToManyField(related_name='_sense_xrefs_+', to='dictionary.Xref'),
        ),
        migrations.AddField(
            model_name='xref',
            name='parent_sense',
            field=models.ManyToManyField(related_name='_xref_parent_sense_+', to='dictionary.Sense'),
        ),
    ]