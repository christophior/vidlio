from django.conf.urls import patterns, include, url
from registration.forms import RegistrationFormUniqueEmail


# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    url(r'^$', 'vidlio.views.home', name='home'),
    url(r'', include('registration.backends.default.urls')),
    url(r'^profile/', include('profiles.urls')),

    # admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    # admin:
    url(r'^admin/', include(admin.site.urls)),

)
