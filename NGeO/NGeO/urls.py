from django.conf.urls import patterns, include, url

from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'NGeO.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^map', 'NGeO.views.map'),
	url(r'^map2', 'NGeO.views.map2'),
	url(r'^index', 'NGeO.views.map2'),
    url(r'^admin/', include(admin.site.urls)),
)
