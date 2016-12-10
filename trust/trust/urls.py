from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'trust.views.home', name='home'),
    # url(r'^trust/', include('trust.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),

    url(r'^admin/', include(admin.site.urls)),
    url(r'^$', include('data.urls')), # for the main pages
    url(r'^users/', include('users.urls')),# once the user logs in...
    url(r'^staff/', include('staff.urls')), # for the staff portal

)
