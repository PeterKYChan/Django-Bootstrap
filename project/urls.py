from django.conf.urls import patterns, include, url
from django.contrib import admin
from django.conf import settings

from experiment.views import *

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'project.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^$', 'experiment.views.index'),
    (r'^accounts/', include('userena.urls')),
    url(r'^admin/', include(admin.site.urls)),
)

if settings.DEBUG:
	# static files (images, css, javascript, etc.)
	urlpatterns += patterns('',(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}))
