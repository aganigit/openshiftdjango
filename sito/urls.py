from django.conf.urls import patterns, include, url
from django.conf import settings
from sito import views
from sito.views import *

urlpatterns = patterns('',
    # Examples:
    url(r'^$', IndexView, name='home'),
    url(r'^(?P<post_id>\d+)/$', DettaglioView, name="dettaglio"),
    url(r'freezer$', FreezerView, name="freezer"),
)