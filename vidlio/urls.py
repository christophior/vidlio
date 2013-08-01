from django.conf.urls import patterns, include, url
from registration.forms import RegistrationFormUniqueEmail


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'vidlio.views.home', name='home'),
    # url(r'^vidlio/', include('vidlio.foo.urls')),
    url(r'', include('registration.backends.default.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^admin/', include(admin.site.urls)),

)
