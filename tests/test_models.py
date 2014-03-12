#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""
test_django-nupages
------------

Tests for `django-nupages` models module.
"""

import os
import shutil
import unittest

from django.utils import timezone
from django.core.urlresolvers import reverse

from nupages import models
from nupages import views


class TestNupages(unittest.TestCase):

	def create_page(
		self, 
		title="Test Page", 
		description="yes, this is only a test", 
		content="yes, this is only a test",
		custom_template=False):
		return models.Page.objects.create(
			title=title, 
			description=description,
			content=content, 
			custom_template=custom_template,
			created=timezone.now())

	def test_page_creation(self):
		p = self.create_page()
		self.assertTrue(isinstance(p, models.Page))
		self.assertEqual(p.__unicode__(), p.title)
		self.assertEqual(p.get_absolute_url(), reverse("nupages:detail", kwargs={'slug': p.slug}))