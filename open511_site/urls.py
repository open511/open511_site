from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

from django.contrib.gis import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'', include('open511.urls')),
    url(r'^map/', include('open511_ui.urls')),
)

urlpatterns += staticfiles_urlpatterns()
