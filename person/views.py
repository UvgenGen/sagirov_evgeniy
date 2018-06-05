# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from person.models import person


def person_list(request):
	persons = person.objects.all()
	return render(request, "person_list.html", 
						{'persons': persons});
