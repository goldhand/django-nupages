# -*- coding: utf-8 -*-
from django.db import models
from django.utils.translation import ugettext_lazy as _

from django_extensions.db.models import TimeStampedModel, TitleSlugDescriptionModel, ActivatorModel


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

	class Meta:
		verbose_name = _('Page')
		verbose_name_plural = _('Pages')
		ordering = ('-created',)

	def get_absolute_url(self):
		return reverse('nupages:detail', kwargs={'slug': self.slug})