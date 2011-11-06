from django.conf.urls.defaults import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from bf3_stat.views import player_awards_view
from bf3_stat.views import player_awards_update_view
from bf3_stat.views import player_view

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()

urlpatterns = staticfiles_urlpatterns()+patterns('',
                        (r'^player/(.+)/update/',player_awards_update_view),
                        (r'^player/(.+)/', player_awards_view),
                        (r'^player/',player_view),
                       
                        
    # Examples:
    # url(r'^$', 'bf3_awards.views.home', name='home'),
    # url(r'^bf3_awards/', include('bf3_awards.foo.urls')),x

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
    
)
