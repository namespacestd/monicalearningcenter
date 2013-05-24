from django.conf.urls import patterns, include, url
from monicalearning.views import *
from django.conf import settings
from django.contrib.staticfiles.urls import staticfiles_urlpatterns

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', home),
    url (r'^site_media/(?P<path>.*)$', 'django.views.static.serve',
        {'document_root': settings.STATIC_ROOT}),
    url(r'^our_program', our_program),
    url(r'^resources', resources),
    url(r'^testimony', testimony),
    url(r'^contact', contact_us),
    url(r'^register', register),
    url(r'^news', news),
    url(r'^admin_news', admin_news),
    url(r'^delete', delete),
    url(r'^login_request', login_request),
    url(r'^logout_request', logout_request),
    # Examples:
    # url(r'^$', 'monicalearning.views.home', name='home'),
    # url(r'^monicalearning/', include('monicalearning.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += staticfiles_urlpatterns()