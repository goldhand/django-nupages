# -*- coding: utf-8 -*-
from django.utils import timezone
from django.db import models
from django.utils.translation import ugettext_lazy as _
from django.core.urlresolvers import reverse

from django_extensions.db.models import TimeStampedModel, TitleSlugDescriptionModel, ActivatorModel
from django_extensions.db.fields import AutoSlugField
from .managers import PageManager


class Tag(models.Model):
	""" Tag
	Provides title and a self-managed "slug" field that populates from the title.
	"""
	title = models.CharField(_('title'), max_length=255)
	slug = AutoSlugField(_('slug'), populate_from='title')

	def __unicode__(self):
		return u'%s' % self.title

	def get_absolute_url(self):
		return reverse('nupages:filter', kwargs={'tag_slug': self.slug})


class Page(TimeStampedModel, TitleSlugDescriptionModel, ActivatorModel):
	""" Page Model 
	Simple page model for creating pages for a website
	inherits the following fields from django_extensions
	"""
	content = models.TextField(blank=True)
	custom_template = models.BooleanField(default=False)
	tags = models.ManyToManyField(Tag, null=True, blank=True)
	public = models.BooleanField(default=False, help_text="If not checked, only registered members will be able to view")

	objects = PageManager()

	class Meta:
		verbose_name = _('Page')
		verbose_name_plural = _('Pages')
		ordering = ('-created',)

	def __unicode__(self):
		return u'%s' % self.title

	def get_absolute_url(self):
		return reverse('nupages:detail', kwargs={'slug': self.slug})