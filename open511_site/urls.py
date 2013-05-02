from django.conf.urls import patterns, include, url
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.views.generic import TemplateView

from django.contrib.gis import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^admin/', include(admin.site.urls)),
    url(r'^api/', include('open511.urls')),
    url(r'^map/', include('open511_ui.urls')),
    url(r'^$', TemplateView.as_view(template_name='open511_home.html')),
    url(r'^accounts/', include('open511_ui.auth_urls')),
)

urlpatterns += staticfiles_urlpatterns()
