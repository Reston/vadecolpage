from django.conf.urls import patterns, include, url
from django.conf import settings
from sitemaps import StaticViewSitemap
# Uncomment the next two lines to enable the admin:
from django.contrib import admin
admin.autodiscover()
sitemaps = {
	'pages': StaticViewSitemap,
}

urlpatterns = patterns(
	'',
	# Examples:
	# url(r'^$', 'vadecol.views.home', name='home'),
	# url(r'^vadecol/', include('vadecol.foo.urls')),

	# Uncomment the admin/doc line below to enable admin documentation:
	# url(r'^admin/doc/', include('django.contrib.admindocs.urls')),

	# Uncomment the next line to enable the admin:
	url(r'^admin/', include(admin.site.urls)),
	url(r'^admin/password_reset/$', 'django.contrib.auth.views.password_reset', name='admin_password_reset'),
	(r'^admin/password_reset/done/$', 'django.contrib.auth.views.password_reset_done'),
	(r'^reset/(?P<uidb36>[0-9A-Za-z]+)-(?P<token>.+)/$', 'django.contrib.auth.views.password_reset_confirm'),
	(r'^reset/done/$', 'django.contrib.auth.views.password_reset_complete'),
)

if settings.DEBUG:
	urlpatterns += patterns(
		'',
		(r'^media/(?P<path>.*)$', 'django.views.static.serve', {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
	)
