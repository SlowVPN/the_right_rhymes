__author__ = 'MBK'

from django.conf.urls import url
from django.contrib import admin


from . import views

urlpatterns = [

    # /
    url(r'^$', views.index, name="dictionary_index"),

    # /admin/
    url(r'^admin/?', admin.site.urls),

    # /statistics/
    url(r"^statistics/$", views.stats, name='stats'),

    # /search-results/
    url(r'^search/$', views.search, name='search'),

    # /search-headwords/
    url(r'^search_headwords/$', views.search_headwords, name='search_headwords'),

    # /about/
    url(r'^about/$', views.about, name='about'),

    # /random/
    url(r'^random/$', views.random_entry, name='random_entry'),

    # /<headword-slug>/
    url(r"^(?P<headword_slug>[a-zA-Z0-9\-_#’']+)/?$", views.entry, name='entry'),

    # /artists/no_image_json/
    url(r"^artists/no_image_json/$", views.artists_no_image_json, name='artists_no_image_json'),

    # /artists/<artist-slug>/
    url(r"^artists/(?P<artist_slug>[a-zA-Z0-9\-_'’,\(\)\+\!ōé½@áó]+)/$", views.artist, name='artist'),

    # /artists/<artist_slug>/json/
    url(r"^artists/(?P<artist_slug>[a-zA-Z0-9\-_'’,\(\)\+\!ōé½@áó]+)/json/$", views.artist_json, name="artist_json"),

    # /artists/<artist_slug>/sense_examples_json/
    url(r"^artists/(?P<artist_slug>[a-zA-Z0-9\-_'’,\(\)\+\!ōé½@áó]+)/sense_examples_json/$", views.artist_sense_examples_json, name="artist_sense_examples_json"),

    # /domains/<domain-slug>/
    url(r"^domains/(?P<domain_slug>[a-zA-Z0-9\-_’']+)/$", views.domain, name='domain'),

    # /domains/<domain-slug>/json/
    url(r"^domains/(?P<domain_slug>[a-zA-Z0-9\-_’']+)/json/$", views.domain_json, name='domain_json'),

    # /semantic-classes/<semantic-class-slug>/
    url(r"^semantic\-classes/(?P<semantic_class_slug>[a-zA-Z0-9\-_’']+)/$", views.semantic_class, name='semantic_class'),

    # /semantic-classes/<semantic-class-slug>/json/
    url(r"^semantic\-classes/(?P<semantic_class_slug>[a-zA-Z0-9\-_’']+)/json/$", views.semantic_class_json, name='semantic_class_json'),

    # /entities/<named-entity-slug>/
    url(r"^entities/(?P<entity_slug>[a-zA-Z0-9\-_'’]+)/$", views.entity, name='entity'),

    # /places/<place-name-slug>/
    url(r"^places/(?P<place_slug>[a-zA-Z0-9\-_'’,\(\)–]+)/$", views.place, name='place'),

    # /places/<place-name-slug>/latlng/
    url(r"^places/(?P<place_slug>[a-zA-Z0-9\-_'’,\(\)]+)/latlng/$", views.place_latlng, name='place_latlng'),

    # /places/<place-name-slug>/artists/json
    url(r"^places/(?P<place_slug>[a-zA-Z0-9\-_'’,\(\)]+)/artists/json/$", views.place_artist_json, name='place_artist_json'),

    # /places/<place-name-slug>/remaining_examples/
    url(r"^places/(?P<place_slug>[a-zA-Z0-9\-_'’,\(\)–]+)/remaining_examples/$", views.remaining_place_examples, name='remaining_place_examples'),

    # /rhymes/<rhyme-slug>/
    url(r"^rhymes/(?P<rhyme_slug>[a-zA-Z0-9\-_#’'éō]+)/?$", views.rhyme, name='rhyme'),

    # /senses/<sense_id>/timeline/
    url(r"^senses/(?P<sense_id>[a-zA-Z0-9_]+)/timeline/$", views.sense_timeline, name='sense_timeline'),

    # /senses/<sense_id>/timeline/json/
    url(r"^senses/(?P<sense_id>[a-zA-Z0-9_]+)/timeline/json/$", views.sense_timeline_json, name="sense_timeline_json"),

    # /senses/<sense_id>/artists/json/
    url(r"^senses/(?P<sense_id>[a-zA-Z0-9_]+)/artists/json/$", views.sense_artists_json, name="sense_artists_json"),

    # /senses/<sense_id>/remaining_examples/
    url(r"^senses/(?P<sense_id>[a-zA-Z0-9_]+)/remaining_examples/$", views.remaining_sense_examples, name="remaining_sense_examples"),

    # /senses/<sense_id>/<artist_slug>/json/
    url(r"^senses/(?P<sense_id>[a-zA-Z0-9_]+)/(?P<artist_slug>[a-zA-Z0-9\-_'’,\(\)]+)/json/$", views.sense_artist_json, name="sense_artist_json"),

    # /songs/<song-slug>/
    url(r"^songs/(?P<song_slug>[a-zA-Z0-9\-_'’,\[\]\(\)\+\!ōóéáñ½#%´=@]+)/$", views.song, name='song'),


]

