from django.conf.urls import patterns, url,include
from django.contrib import admin
from django.conf import settings
urlpatterns = patterns('',url(r'^admin/', include(admin.site.urls)),
    # Examples:
    # url(r'^$', 'tango_with_django_project_17.views.home', name='home'),
    # url(r'^blog/', include('blog.urls')),
    url(r'^rango/', include('rango.urls')), # ADD THIS NEW TUPLE!
)
if settings.DEBUG:
    urlpatterns += patterns(
        'django.views.static',
        (r'^media/(?P<path>.*)',
        'serve',
        {'document_root': settings.MEDIA_ROOT}), )
