# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django import forms
from django.forms import ModelForm
from person.models import Person, Curse
from django.contrib import messages


class PersonForm(ModelForm):
	class Meta:
		fields = "__all__"
		model = Person
		widgets = {'curse': forms.SelectMultiple }

def person_list(request):
	persons = Person.objects.all()
	return render(request, "person_list.html", 
						{'persons': persons},);

def person_info(request, num):
	persons = Person.objects.get(id = int(num))
	return render(request, "person.html", 
						{'persons': persons},);

def addPerson(request):
	form = PersonForm()
	if request.method == 'POST':
		form = PersonForm(request.POST)
		if form.is_valid():
			newPerson = form.save()
			messages.success(request, 'Save!')
			return redirect('addPerson')
			
	else:	
		form = PersonForm()

	return render(request, "addPerson.html", 
						{'forms': form},);


def curse_list(request):
	curs = Curse.objects.all()
	return render(request, "curse_list.html", 
						{'curses': curs},);

def curse_info(request, num): 
	curs = Curse.objects.get(id = int(num))
	return render(request, "curse.html", 
						{'curses': curs});
