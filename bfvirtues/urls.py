from django.conf.urls import patterns, include, url
import settings
from app import views

# Uncomment the next two lines to enable the admin:
# from django.contrib import admin
# admin.autodiscover()


urlpatterns = patterns('',

    url(r'', include('social_auth.urls')),

    # (r'^admin/', include(admin.site.urls)),
    (r'media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT}),

    # Examples:
    url(r'^$', views.index),
    url(r'^home/$', views.home),
    url(r'^logged-in/$', views.logged_in),
    url(r'^update_virtue/(.*)/$', views.update_virtue)
    # url(r'^bfvirtues/', include('bfvirtues.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    # url(r'^admin/', include(admin.site.urls)),
)
