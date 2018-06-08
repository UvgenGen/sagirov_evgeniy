# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render
from person.models import person, curse


def person_list(request):
	persons = person.objects.all()
	return render(request, "person_list.html", 
						{'persons': persons},);

def curse_list(request):
	curs = curse.objects.all()
	return render(request, "curse_list.html", 
						{'curses': curs},);

def curse_info(request, num):
	curs = curse.objects.get(id = int(num))
	return render(request, "curse.html", 
						{'curses': curs});

def person_info(request, num):
	persons = person.objects.get(id = int(num))
	return render(request, "person.html", 
						{'persons': persons},);