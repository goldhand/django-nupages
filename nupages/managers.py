# -*- coding: utf-8 -*-
from django.db import models
from django.db.models import Q
from django.utils import timezone


class PageManager(models.Manager):

	def published(self, **kwargs):
		""" Returns pages that are both status: Active and have a non-conflicting activate_date / deactivate_date 
			TODO: Write tests for this
		"""
		return self.filter(
			Q(activate_date__lte=timezone.now()) | Q(activate_date__isnull=True),
			Q(deactivate_date__gte=timezone.now()) | Q(deactivate_date__isnull=True),
			Q(status=1), **kwargs)
