#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_django-nupages
------------

Tests for `django-nupages` views module.
"""

from django.test import TestCase
from django.utils import timezone
from django.core.urlresolvers import reverse
#from .forms import PageFor
from nupages import models
from nupages import views


class PageTest(TestCase):

	def create_page(
		self, 
		title="Test Page", 
		description="yes, this is only a test", 
		content="yes, this is only a test",
		custom_template=False,
		activate_date=timezone.now(),
		status=1):
		return models.Page.objects.create(
			title=title, 
			description=description,
			content=content, 
			custom_template=custom_template,
			created=timezone.now(),
			activate_date=activate_date,
			status = status
			)

	def test_page_list_view(self):
		p = self.create_page(title="List View Test Page")
		url = reverse("nupages:list")
		resp = self.client.get(url)

		self.assertEqual(resp.status_code, 200)

	def test_page_detail_view(self):
		p = self.create_page(title="Detail View Test Page")
		url = reverse('nupages:detail', kwargs={'slug': p.slug})
		resp = self.client.get(url)

		self.assertEqual(resp.status_code, 200)
		self.assertIn(p.title, resp.content)

	def test_page_custom_template(self):
		p = self.create_page(
			title="Test Page Custom Template",
			custom_template=True)
		url = reverse('nupages:detail', kwargs={'slug': p.slug})
		resp = self.client.get(url)

		self.assertEqual(resp.status_code, 200)
		self.assertIn(p.title, resp.content)

