import datetime

from django.db import models
from django.utils import timezone
from django.contrib.postgres.fields import JSONField


class Entry(models.Model):
    headword = models.CharField(primary_key=True, max_length=200)
    letter = models.CharField(max_length=1, null=True, blank=True)
    slug = models.SlugField('Headword Slug')
    publish = models.BooleanField(default=False)
    pub_date = models.DateTimeField('Date Published', auto_now_add=True, blank=True)
    last_updated = models.DateField('Last Updated', auto_now=True, null=True, blank=True)
    json = JSONField(null=True, blank=True)
    image = models.ForeignKey('Image', on_delete=models.CASCADE, related_name="entry_image", null=True, blank=True)
    senses = models.ManyToManyField('Sense', related_name='+', blank=True)

    class Meta:
        ordering = ["headword"]
        verbose_name_plural = "Entries"

    def __str__(self):
        return self.headword

    def published_recently(self):
        return self.pub_date >= timezone.now() - datetime.timedelta(days=1)


class Editor(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField('Editor Name', max_length=1000)
    slug = models.SlugField('Slug')

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Image(models.Model):
    id = models.AutoField(primary_key=True)
    title = models.CharField('Image Title', max_length=1000)
    slug = models.SlugField('Slug')
    image = models.ImageField()

    class Meta:
        ordering = ["title"]

    def __str__(self):
        return self.title


class Artist(models.Model):
    name = models.CharField(primary_key=True, max_length=1000)
    slug = models.SlugField('Artist Slug')
    origin = models.ManyToManyField('Place', related_name="+")
    image = models.ForeignKey(Image, on_delete=models.CASCADE, related_name="depicts", null=True, blank=True)
    primary_examples = models.ManyToManyField('Example', related_name="+")
    primary_senses = models.ManyToManyField('Sense', related_name="+")
    featured_examples = models.ManyToManyField('Example', related_name="+")
    featured_senses = models.ManyToManyField('Sense', related_name="+")

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Place(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=1000)
    slug = models.CharField('Place Slug', max_length=1000, null=True, blank=True)
    latitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    longitude = models.DecimalField(max_digits=9, decimal_places=6, null=True, blank=True)
    artists = models.ManyToManyField(Artist, through=Artist.origin.through, related_name="+")

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class Sense(models.Model):
    id = models.AutoField(primary_key=True)
    headword = models.CharField('Headword', max_length=200, null=True, blank=True)
    slug = models.SlugField('Sense Slug', null=True, blank=True)
    xml_id = models.CharField('XML id', max_length=20, null=True, blank=True)
    part_of_speech = models.CharField('Part of Speech', max_length=20)
    json = JSONField(null=True, blank=True)
    parent_entry = models.ManyToManyField(Entry, through=Entry.senses.through, related_name="+")
    definition = models.CharField(max_length=2000, null=True, blank=True)
    etymology = models.CharField(max_length=2000, null=True, blank=True)
    notes = models.CharField(max_length=2000, null=True, blank=True)
    examples = models.ManyToManyField('Example', related_name="+")
    domains = models.ManyToManyField('Domain', related_name="+")
    synset = models.ManyToManyField('SynSet', related_name="+")
    xrefs = models.ManyToManyField('Xref', related_name="+")
    rhymes = models.ManyToManyField('Rhyme', related_name="+")
    collocates = models.ManyToManyField('Collocate', related_name="+")
    features_entities = models.ManyToManyField('NamedEntity', related_name="+")
    cites_artists = models.ManyToManyField(Artist, through=Artist.featured_senses.through, related_name="+")

    class Meta:
        ordering = ["xml_id"]

    def __str__(self):
        return self.headword + ', ' + self.part_of_speech + ' (' + self.xml_id + ')'


class Example(models.Model):
    id = models.AutoField(primary_key=True)
    artist = models.ManyToManyField(Artist, through=Artist.primary_examples.through, related_name="+")
    artist_name = models.CharField('Artist Name', max_length=200, null=True, blank=True)
    artist_slug = models.SlugField('Artist Slug', blank=True, null=True)
    song_title = models.CharField('Song Title', max_length=200)
    feat_artist = models.ManyToManyField(Artist, through=Artist.featured_examples.through, related_name="+")
    release_date = models.DateField('Release Date', blank=True, null=True)
    release_date_string = models.CharField('Release Date String', max_length=10, blank=True, null=True)
    album = models.CharField('Album', max_length=200)
    lyric_text = models.CharField('Lyric Text', max_length=1000)
    json = JSONField(null=True, blank=True)
    illustrates_senses = models.ManyToManyField(Sense, through=Sense.examples.through, related_name="+")
    features_entities = models.ManyToManyField('NamedEntity', related_name="+")
    lyric_links = models.ManyToManyField('LyricLink', related_name="+")

    class Meta:
        ordering = ["release_date", "artist_name"]

    def __str__(self):
        return '[' + str(self.release_date_string) + '] ' + str(self.artist_name) + ' - ' + str(self.lyric_text)


class SynSet(models.Model):
    name = models.CharField(primary_key=True, max_length=1000)
    slug = models.SlugField('SynSet Slug', blank=True, null=True)
    senses = models.ManyToManyField('Sense', through=Sense.synset.through, related_name='+', blank=True)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "SynSets"

    def __str__(self):
        return self.name


class Domain(models.Model):
    name = models.CharField(primary_key=True, max_length=1000)
    slug = models.SlugField('Domain Slug', blank=True, null=True)
    senses = models.ManyToManyField('Sense', through=Sense.domains.through, related_name='+', blank=True)

    class Meta:
        ordering = ["name"]

    def __str__(self):
        return self.name


class NamedEntity(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=1000, blank=True, null=True)
    slug = models.SlugField('Entity Slug', blank=True, null=True)
    pref_label = models.CharField(max_length=1000, blank=True, null=True)
    pref_label_slug = models.SlugField('Entity PrefLabel Slug', blank=True, null=True)
    entity_type = models.CharField(max_length=1000, blank=True, null=True)
    mentioned_at_senses = models.ManyToManyField(Sense, through=Sense.features_entities.through, related_name="+", blank=True)
    examples = models.ManyToManyField(Example, through=Example.features_entities.through, related_name='+', blank=True)

    class Meta:
        ordering = ["name"]
        verbose_name_plural = "Named Entities"

    def __str__(self):
        return self.name


class Xref(models.Model):
    id = models.AutoField(primary_key=True)
    xref_word = models.CharField(max_length=1000, blank=True, null=True)
    xref_type = models.CharField(max_length=1000, blank=True, null=True)
    target_lemma = models.CharField(max_length=1000, blank=True, null=True)
    target_slug = models.SlugField(blank=True, null=True)
    target_id = models.CharField(max_length=1000, blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    frequency = models.IntegerField(blank=True, null=True)
    parent_sense = models.ManyToManyField(Sense, through=Sense.xrefs.through, related_name="+")

    class Meta:
        ordering = ["xref_word"]

    def __str__(self):
        return self.xref_word


class Collocate(models.Model):
    id = models.AutoField(primary_key=True)
    collocate_lemma = models.CharField(max_length=1000, blank=True, null=True)
    source_sense_xml_id = models.CharField('Source XML ID', max_length=20, null=True, blank=True)
    target_slug = models.SlugField(blank=True, null=True)
    target_id = models.CharField(max_length=1000, blank=True, null=True)
    frequency = models.IntegerField(blank=True, null=True)
    parent_sense = models.ManyToManyField(Sense, through=Sense.collocates.through, related_name="+")

    class Meta:
        ordering = ["collocate_lemma"]

    def __str__(self):
        return self.collocate_lemma


class Rhyme(models.Model):
    id = models.AutoField(primary_key=True)
    rhyme_word = models.CharField(max_length=1000, blank=True, null=True)
    source_sense_xml_id = models.CharField('Source XML ID', max_length=20, null=True, blank=True)
    target_slug = models.SlugField(blank=True, null=True)
    target_id = models.CharField(max_length=1000, blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    frequency = models.IntegerField(blank=True, null=True)
    parent_sense = models.ManyToManyField(Sense, through=Sense.rhymes.through, related_name="+")

    class Meta:
        ordering = ["rhyme_word"]

    def __str__(self):
        return self.rhyme_word


class LyricLink(models.Model):
    id = models.AutoField(primary_key=True)
    link_type = models.CharField(max_length=1000, blank=True, null=True)
    link_text = models.CharField(max_length=1000, blank=True, null=True)
    target_lemma = models.CharField(max_length=1000, blank=True, null=True)
    target_slug = models.SlugField(blank=True, null=True)
    position = models.IntegerField(blank=True, null=True)
    parent_example = models.ManyToManyField(Example, through=Example.lyric_links.through, related_name="+")

    class Meta:
        ordering = ["link_text"]

    def __str__(self):
        return self.link_text

