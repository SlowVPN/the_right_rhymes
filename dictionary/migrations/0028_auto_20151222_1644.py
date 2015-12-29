# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2015-12-22 16:44
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dictionary', '0027_auto_20151222_1643'),
    ]

    operations = [
        migrations.CreateModel(
            name='Entity',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=1000, null=True)),
                ('pref_label', models.CharField(blank=True, max_length=1000, null=True)),
                ('entity_type', models.CharField(blank=True, max_length=1000, null=True)),
                ('examples', models.ManyToManyField(blank=True, related_name='_entity_examples_+', to='dictionary.Example')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name_plural': 'Entities',
            },
        ),
        migrations.AddField(
            model_name='example',
            name='features_entities',
            field=models.ManyToManyField(related_name='_example_features_entities_+', to='dictionary.Entity'),
        ),
    ]