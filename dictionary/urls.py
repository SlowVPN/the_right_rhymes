__author__ = 'MBK'

from django.conf.urls import url
from django.contrib import admin


from . import views

urlpatterns = [

    # /admin/
    url(r'^admin/?', admin.site.urls),

    # /
    url(r'^$', views.index, name="dictionary_index"),

    # /statistics/
    url(r"^statistics/?$", views.stats, name='stats'),

    # /search-results/
    url(r'^search/$', views.search, name='search'),

    # /headword-as-a-slug/
    url(r"^(?P<headword_slug>[a-zA-Z0-9\-_#’']+)/?$", views.entry, name='entry'),

    # /artist-name-as-a-slug/
    url(r"^artists/(?P<artist_slug>[a-zA-Z0-9\-_'’,\(\)]+)/$", views.artist, name='artist'),

    url(r"^senses/(?P<sense_id>[a-zA-Z0-9_]+)/artist_origins/$", views.sense_artist_origins, name="sense_artist_origins"),

    # /place-name-as-a-slug/
    url(r"^places/(?P<place_slug>[a-zA-Z0-9\-_'’,\(\)]+)/$", views.place, name='place'),

    # /domain-as-a-slug/
    url(r"^domains/(?P<domain_slug>[a-zA-Z0-9\-_’']+)/$", views.domain, name='domain'),

    # /named-entity-as-a-slug/
    url(r"^entities/(?P<entity_slug>[a-zA-Z0-9\-_'’]+)/$", views.entity, name='entity'),

]

