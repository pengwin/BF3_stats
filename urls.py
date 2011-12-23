import settings
from django.conf.urls.defaults import patterns
from django.conf.urls.defaults import url
from django.conf.urls.defaults import include
from django.contrib.staticfiles.urls import staticfiles_urlpatterns


from views_ajax import player_ajax_test
from views_ajax import player_search

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = 	patterns('',
                        url(r'^bf3_stat/', include('bf3_stat.urls')),

    # Examples:
    # url(r'^$', 'bf3_awards.views.home', name='home'),
    # url(r'^bf3_awards/', include('bf3_awards.foo.urls')),x

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
	urlpatterns += staticfiles_urlpatterns()
