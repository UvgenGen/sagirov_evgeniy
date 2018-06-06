# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models


class person(models.Model):
	name = models.CharField(max_length=255)
	surname = models.CharField(max_length=255)
	date_of_birth = models.DateField(max_length=255)
	email = models.EmailField()
	phone = models.CharField(max_length=255)

