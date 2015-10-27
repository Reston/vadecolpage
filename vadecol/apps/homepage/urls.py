from django.conf.urls import patterns, url

urlpatterns = patterns(
	'vadecol.apps.homepage.views',
	url(r'^$', 'index', name="homepageindex"),
	url(r'^quienes-somos/$', 'quienessomos', name="homepageabout"),
	url(r'^servicios/$', 'services', name="homepageservices"),
	url(r'^contacto/$', 'contact', name="homapagecontact"),
)
