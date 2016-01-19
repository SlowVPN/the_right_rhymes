# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-19 13:21
from __future__ import unicode_literals

import django.contrib.postgres.fields.jsonb
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('name', models.CharField(max_length=1000, primary_key=True, serialize=False)),
                ('slug', models.SlugField(verbose_name='Artist Slug')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Collocate',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('collocate_lemma', models.CharField(blank=True, max_length=1000, null=True)),
                ('source_sense_xml_id', models.CharField(blank=True, max_length=20, null=True, verbose_name='Source XML ID')),
                ('target_slug', models.SlugField(blank=True, null=True)),
                ('target_id', models.CharField(blank=True, max_length=1000, null=True)),
                ('frequency', models.IntegerField(blank=True, null=True)),
            ],
            options={
                'ordering': ['collocate_lemma'],
            },
        ),
        migrations.CreateModel(
            name='Domain',
            fields=[
                ('name', models.CharField(max_length=1000, primary_key=True, serialize=False)),
                ('slug', models.SlugField(blank=True, null=True, verbose_name='Domain Slug')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Editor',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=1000, verbose_name='Editor Name')),
                ('slug', models.SlugField(verbose_name='Slug')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Entry',
            fields=[
                ('headword', models.CharField(max_length=200, primary_key=True, serialize=False)),
                ('letter', models.CharField(blank=True, max_length=1, null=True)),
                ('slug', models.SlugField(verbose_name='Headword Slug')),
                ('publish', models.BooleanField(default=False)),
                ('pub_date', models.DateTimeField(auto_now_add=True, verbose_name='Date Published')),
                ('last_updated', models.DateField(auto_now=True, null=True, verbose_name='Last Updated')),
                ('json', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
            ],
            options={
                'ordering': ['headword'],
                'verbose_name_plural': 'Entries',
            },
        ),
        migrations.CreateModel(
            name='Example',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('artist_name', models.CharField(blank=True, max_length=200, null=True, verbose_name='Artist Name')),
                ('artist_slug', models.SlugField(blank=True, null=True, verbose_name='Artist Slug')),
                ('song_title', models.CharField(max_length=200, verbose_name='Song Title')),
                ('release_date', models.DateField(blank=True, null=True, verbose_name='Release Date')),
                ('release_date_string', models.CharField(blank=True, max_length=10, null=True, verbose_name='Release Date String')),
                ('album', models.CharField(max_length=200, verbose_name='Album')),
                ('lyric_text', models.CharField(max_length=1000, verbose_name='Lyric Text')),
                ('json', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('artist', models.ManyToManyField(related_name='_example_artist_+', to='dictionary.Artist')),
            ],
            options={
                'ordering': ['release_date', 'artist_name'],
            },
        ),
        migrations.CreateModel(
            name='ExampleRhyme',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('word_one', models.CharField(blank=True, max_length=1000, null=True)),
                ('word_two', models.CharField(blank=True, max_length=1000, null=True)),
                ('word_one_slug', models.SlugField(blank=True, null=True)),
                ('word_two_slug', models.SlugField(blank=True, null=True)),
                ('word_one_target_id', models.CharField(blank=True, max_length=1000, null=True)),
                ('word_two_target_id', models.CharField(blank=True, max_length=1000, null=True)),
                ('word_one_position', models.IntegerField(blank=True, null=True)),
                ('word_two_position', models.IntegerField(blank=True, null=True)),
                ('parent_example', models.ManyToManyField(related_name='_examplerhyme_parent_example_+', to='dictionary.Example')),
            ],
            options={
                'ordering': ['word_one', 'word_two'],
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('title', models.CharField(max_length=1000, verbose_name='Image Title')),
                ('slug', models.SlugField(verbose_name='Slug')),
                ('image', models.ImageField(upload_to='')),
            ],
            options={
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='LyricLink',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('link_type', models.CharField(blank=True, max_length=1000, null=True)),
                ('link_text', models.CharField(blank=True, max_length=1000, null=True)),
                ('target_lemma', models.CharField(blank=True, max_length=1000, null=True)),
                ('target_slug', models.SlugField(blank=True, null=True)),
                ('position', models.IntegerField(blank=True, null=True)),
                ('parent_example', models.ManyToManyField(related_name='_lyriclink_parent_example_+', to='dictionary.Example')),
            ],
            options={
                'ordering': ['link_text'],
            },
        ),
        migrations.CreateModel(
            name='NamedEntity',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(blank=True, max_length=1000, null=True)),
                ('slug', models.SlugField(blank=True, null=True, verbose_name='Entity Slug')),
                ('pref_label', models.CharField(blank=True, max_length=1000, null=True)),
                ('pref_label_slug', models.SlugField(blank=True, null=True, verbose_name='Entity PrefLabel Slug')),
                ('entity_type', models.CharField(blank=True, max_length=1000, null=True)),
                ('examples', models.ManyToManyField(blank=True, related_name='_namedentity_examples_+', to='dictionary.Example')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name_plural': 'Named Entities',
            },
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=1000)),
                ('slug', models.CharField(blank=True, max_length=1000, null=True, verbose_name='Place Slug')),
                ('latitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('longitude', models.DecimalField(blank=True, decimal_places=6, max_digits=9, null=True)),
                ('artists', models.ManyToManyField(related_name='_place_artists_+', to='dictionary.Artist')),
            ],
            options={
                'ordering': ['name'],
            },
        ),
        migrations.CreateModel(
            name='Sense',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('headword', models.CharField(blank=True, max_length=200, null=True, verbose_name='Headword')),
                ('slug', models.SlugField(blank=True, null=True, verbose_name='Sense Slug')),
                ('xml_id', models.CharField(blank=True, max_length=20, null=True, verbose_name='XML id')),
                ('part_of_speech', models.CharField(max_length=20, verbose_name='Part of Speech')),
                ('json', django.contrib.postgres.fields.jsonb.JSONField(blank=True, null=True)),
                ('definition', models.CharField(blank=True, max_length=2000, null=True)),
                ('etymology', models.CharField(blank=True, max_length=2000, null=True)),
                ('notes', models.CharField(blank=True, max_length=2000, null=True)),
                ('cites_artists', models.ManyToManyField(related_name='_sense_cites_artists_+', to='dictionary.Artist')),
                ('collocates', models.ManyToManyField(blank=True, related_name='_sense_collocates_+', to='dictionary.Collocate')),
                ('domains', models.ManyToManyField(related_name='_sense_domains_+', to='dictionary.Domain')),
                ('examples', models.ManyToManyField(related_name='_sense_examples_+', to='dictionary.Example')),
                ('features_entities', models.ManyToManyField(related_name='_sense_features_entities_+', to='dictionary.NamedEntity')),
                ('parent_entry', models.ManyToManyField(related_name='_sense_parent_entry_+', to='dictionary.Entry')),
            ],
            options={
                'ordering': ['xml_id'],
            },
        ),
        migrations.CreateModel(
            name='SenseRhyme',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('rhyme', models.CharField(blank=True, max_length=1000, null=True)),
                ('rhyme_slug', models.SlugField(blank=True, null=True)),
                ('parent_sense_xml_id', models.CharField(blank=True, max_length=20, null=True, verbose_name='Source XML ID')),
                ('frequency', models.IntegerField(blank=True, null=True)),
                ('parent_sense', models.ManyToManyField(related_name='_senserhyme_parent_sense_+', to='dictionary.Sense')),
            ],
            options={
                'ordering': ['rhyme'],
            },
        ),
        migrations.CreateModel(
            name='SynSet',
            fields=[
                ('name', models.CharField(max_length=1000, primary_key=True, serialize=False)),
                ('slug', models.SlugField(blank=True, null=True, verbose_name='SynSet Slug')),
                ('senses', models.ManyToManyField(blank=True, related_name='_synset_senses_+', to='dictionary.Sense')),
            ],
            options={
                'ordering': ['name'],
                'verbose_name_plural': 'SynSets',
            },
        ),
        migrations.CreateModel(
            name='Xref',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('xref_word', models.CharField(blank=True, max_length=1000, null=True)),
                ('xref_type', models.CharField(blank=True, max_length=1000, null=True)),
                ('target_lemma', models.CharField(blank=True, max_length=1000, null=True)),
                ('target_slug', models.SlugField(blank=True, null=True)),
                ('target_id', models.CharField(blank=True, max_length=1000, null=True)),
                ('position', models.IntegerField(blank=True, null=True)),
                ('frequency', models.IntegerField(blank=True, null=True)),
                ('parent_sense', models.ManyToManyField(related_name='_xref_parent_sense_+', to='dictionary.Sense')),
            ],
            options={
                'ordering': ['xref_word'],
            },
        ),
        migrations.AddField(
            model_name='sense',
            name='sense_rhymes',
            field=models.ManyToManyField(blank=True, related_name='_sense_sense_rhymes_+', to='dictionary.SenseRhyme'),
        ),
        migrations.AddField(
            model_name='sense',
            name='synset',
            field=models.ManyToManyField(related_name='_sense_synset_+', to='dictionary.SynSet'),
        ),
        migrations.AddField(
            model_name='sense',
            name='xrefs',
            field=models.ManyToManyField(related_name='_sense_xrefs_+', to='dictionary.Xref'),
        ),
        migrations.AddField(
            model_name='namedentity',
            name='mentioned_at_senses',
            field=models.ManyToManyField(blank=True, related_name='_namedentity_mentioned_at_senses_+', to='dictionary.Sense'),
        ),
        migrations.AddField(
            model_name='example',
            name='example_rhymes',
            field=models.ManyToManyField(related_name='_example_example_rhymes_+', to='dictionary.ExampleRhyme'),
        ),
        migrations.AddField(
            model_name='example',
            name='feat_artist',
            field=models.ManyToManyField(related_name='_example_feat_artist_+', to='dictionary.Artist'),
        ),
        migrations.AddField(
            model_name='example',
            name='features_entities',
            field=models.ManyToManyField(related_name='_example_features_entities_+', to='dictionary.NamedEntity'),
        ),
        migrations.AddField(
            model_name='example',
            name='illustrates_senses',
            field=models.ManyToManyField(related_name='_example_illustrates_senses_+', to='dictionary.Sense'),
        ),
        migrations.AddField(
            model_name='example',
            name='lyric_links',
            field=models.ManyToManyField(related_name='_example_lyric_links_+', to='dictionary.LyricLink'),
        ),
        migrations.AddField(
            model_name='entry',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='entry_image', to='dictionary.Image'),
        ),
        migrations.AddField(
            model_name='entry',
            name='senses',
            field=models.ManyToManyField(blank=True, related_name='_entry_senses_+', to='dictionary.Sense'),
        ),
        migrations.AddField(
            model_name='domain',
            name='senses',
            field=models.ManyToManyField(blank=True, related_name='_domain_senses_+', to='dictionary.Sense'),
        ),
        migrations.AddField(
            model_name='collocate',
            name='parent_sense',
            field=models.ManyToManyField(related_name='_collocate_parent_sense_+', to='dictionary.Sense'),
        ),
        migrations.AddField(
            model_name='artist',
            name='featured_examples',
            field=models.ManyToManyField(related_name='_artist_featured_examples_+', to='dictionary.Example'),
        ),
        migrations.AddField(
            model_name='artist',
            name='featured_senses',
            field=models.ManyToManyField(related_name='_artist_featured_senses_+', to='dictionary.Sense'),
        ),
        migrations.AddField(
            model_name='artist',
            name='image',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='depicts', to='dictionary.Image'),
        ),
        migrations.AddField(
            model_name='artist',
            name='origin',
            field=models.ManyToManyField(related_name='_artist_origin_+', to='dictionary.Place'),
        ),
        migrations.AddField(
            model_name='artist',
            name='primary_examples',
            field=models.ManyToManyField(related_name='_artist_primary_examples_+', to='dictionary.Example'),
        ),
        migrations.AddField(
            model_name='artist',
            name='primary_senses',
            field=models.ManyToManyField(related_name='_artist_primary_senses_+', to='dictionary.Sense'),
        ),
    ]
