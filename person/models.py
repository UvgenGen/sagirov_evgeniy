# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class curse(models.Model):
	name = models.CharField(max_length=255)
	info = models.TextField()

	def __unicode__(self):
		return self.name

class person(models.Model):
	name = models.CharField(max_length=255)
	surname = models.CharField(max_length=255)
	date_of_birth = models.DateField()
	email = models.EmailField()
	phone = models.CharField(max_length=255)
	curse = models.ManyToManyField(curse)

