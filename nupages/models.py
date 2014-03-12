# -*- coding: utf-8 -*-
from django.utils import timezone
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from django_extensions.db.models import TimeStampedModel, TitleSlugDescriptionModel, ActivatorModel

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
	custom_template = models.BooleanField(default=False)

	objects = PageManager()

	class Meta:
		verbose_name = _('Page')
		verbose_name_plural = _('Pages')
		ordering = ('-created',)

	def __unicode__(self):
		return u'%s' % self.title

	def get_absolute_url(self):
		return reverse('nupages:detail', kwargs={'slug': self.slug})