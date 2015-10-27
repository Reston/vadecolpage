#-*- encoding: utf-8 -*-
from django.contrib import sitemaps
from django.core.urlresolvers import reverse


class StaticViewSitemap(sitemaps.Sitemap):
	priority = 0.5
	changefreq = 'montly'

	def items(self):
		return [
				'homepageindex',
				'homepageabout',
				'homepageservices',
				'homepagecontact',
				# colocar los nombre de las url en este lugar. ejemplo: 'homepageworks'
				]

	def location(self, item):
		return reverse(item)
