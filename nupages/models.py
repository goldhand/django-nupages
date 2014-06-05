# -*- coding: utf-8 -*-
from django.db import models
from django.db.models import permalink
from django.utils.translation import ugettext_lazy as _
from django.contrib.sites.models import Site

from django_extensions.db.models import TimeStampedModel, TitleSlugDescriptionModel, ActivatorModel
import positions

from .managers import PageManager


class Page(TimeStampedModel, TitleSlugDescriptionModel, ActivatorModel):
	""" Page Model 
	Simple page model for creating pages for a website
	inherits the following fields from django_extensions:
		created
		modified
		title
		slug
		description
		status
		activate_date
		deactivate_date
	"""
	content = models.TextField(blank=True)
	custom_template = models.CharField(max_length=255, blank=True, 
		help_text="Example: 'nupages/page.html'. If this isn't provided, the system will use 'nupages/page_detail.html'.")
	site = models.ForeignKey(Site)
	order = positions.PositionField()

	objects = PageManager()

	class Meta:
		verbose_name = _('Page')
		verbose_name_plural = _('Pages')
		ordering = ['order',]
		get_latest_by = 'order'
		order_with_respect_to = 'site'

	def __unicode__(self):
		return u'%s' % self.title

	@permalink
	def get_absolute_url(self):
		return 'nupages:detail', (), {'slug': self.slug}
