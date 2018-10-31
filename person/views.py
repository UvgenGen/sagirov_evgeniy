# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.shortcuts import render, redirect
from django import forms
from django.forms import ModelForm
from person.models import Person, Curse
from django.contrib import messages
from django.views.generic import ListView, DetailView, FormView, CreateView, UpdateView, DeleteView


class PersonForm(ModelForm):
	class Meta:
		fields = "__all__"
		model = Person
		widgets = {'curse': forms.SelectMultiple }

class CurseList(ListView):
	model = Curse
	template_name = 'curse/curse_list.html'

class CurseDetailView(DetailView):
    model = Curse
    template_name = 'curse/curse.html'
    context_object_name = 'curse'

class Personlist(ListView):
	model = Person
	context_object_name = 'curse'
	paginate_by = 5

class PersonDetailView(DetailView):
    model = Person
    template_name = "person.html"
    context_object_name = 'person'

class EditPerson(UpdateView):
	model = Person
	template_name = 'edit_person.html'
	form_class = PersonForm
	success_url = 'edit_person'

	def form_valid(self, form):
		messages.success(self.request, 'Save!')
		return super(EditPerson, self).form_valid(form)

class DeletePerson(DeleteView):
	model = Person
	template_name = 'delete_person.html'
	form_class = PersonForm
	success_url = 'delete_person'

	def form_valid(self, form):
		messages.success(self.request, 'Save!')
		return super(DeletePerson, self).form_valid(form)

class AddPerson(CreateView):
	model = Person
	template_name = 'addPerson.html'
	form_class = PersonForm
	success_url = 'person'

	def form_valid(self, form):
		messages.success(self.request, 'Save!')
		return super(AddPerson, self).form_valid(form)