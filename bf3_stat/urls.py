"""
Urls specific for bf3stat app
"""
__author__ = 'pengwin4'

from django.conf.urls.defaults import patterns
from views.jquery_views import index_view
from views.jquery_views import player_awards_view
from views.jquery_views import player_update_view

urlpatterns = patterns('',
                (r'^player/(.+)/update/',player_update_view),
                (r'^player/(.+)/', player_awards_view),
                (r'^player/',index_view),
)