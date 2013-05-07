from django.conf.urls import patterns, include, url

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'staticpages.views.home', name='home'),
    # url(r'^staticpages/', include('staticpages.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
)

urlpatterns += patterns('django.contrib.flatpages.views',
    url(r'^/$', 'flatpage', {'url': '//'}, name='home'),
    url(r'^about/$', 'flatpage', {'url': '/about/'}, name='about'),
    url(r'^help/$', 'flatpage', {'url': '/license/'}, name='license'),
) 
