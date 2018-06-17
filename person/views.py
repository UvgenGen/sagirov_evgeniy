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

def person_info(request, pk):
	persons = Person.objects.get(id=pk)
	return render(request, "person.html", 
						{'persons': persons},);

def add_person(request):
	form = PersonForm()
	if request.method == 'POST':
		form = PersonForm(request.POST)
		if form.is_valid():
			newPerson = form.save()
			messages.success(request, 'Save!')
			return redirect('person')
			
	else:	
		form = PersonForm()

	return render(request, "addPerson.html", 
						{'forms': form},);

def edit_person(request, pk):
	person = Person.objects.get(id=pk)
	if request.method == 'POST':
		form = PersonForm(request.POST, instance=person)
		if form.is_valid():
			newPerson = form.save()
			messages.success(request, 'Save!')
			return redirect('person')
			
	else:	
		form = PersonForm(instance=person)

	return render(request, "edit_person.html", 
						{'forms': form},);	

def delete_person(request, pk):
	person = Person.objects.get(id=pk)
	if request.method == 'POST':
		messages.success(request, 'Delete!')
		return redirect('person')

	return render(request, "delete_person.html", 
						{'person': person},);	

def curse_list(request):
	curs = Curse.objects.all()
	return render(request, "curse_list.html", 
						{'curses': curs},);

def curse_info(request, pk): 
	curs = Curse.objects.get(id=pk)
	return render(request, "curse.html", 
						{'curses': curs});
