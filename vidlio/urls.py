from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    url(r'^$', 'vidlio.views.home', name='home'),
    # url(r'^vidlio/', include('vidlio.foo.urls')),
    url(r'', include('registration.backends.default.urls')),

<<<<<<< HEAD
    # Uncomment the admin/doc line below to enable admin documentation:
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
=======
    url(r'^admin/doc/', include('django.contrib.admindocs.urls')),
    url(r'^grappelli/', include('grappelli.urls')),
>>>>>>> f676ec14194b28199658d4e7fe54d0db3101cf60
    url(r'^admin/', include(admin.site.urls)),
)
