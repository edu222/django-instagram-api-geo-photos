from django.conf.urls import patterns, include, url
from django.contrib.auth.views import login, logout

# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()

urlpatterns = patterns('',
    # Examples:
    # url(r'^$', 'udla_web_app.views.home', name='home'),
    # url(r'^udla_web_app/', include('udla_web_app.foo.urls')),

    # Uncomment the admin/doc line below to enable admin documentation:
    # url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

    # Uncomment the next line to enable the admin:
    url(r'^admin/', include(admin.site.urls)),
    url(r'^accounts/', include('registration.backends.default.urls')),
    url(r'^$', 'core.views.app_index', name='index'),
    url(r'^lugares/(?P<locationslug>.*)/$','core.views.location_page'),
    url(r'^search/', 'core.views.search_locations'),
    url(r'^accounts/login/$',  login),
    url(r'^accounts/logout/$', logout),
)
