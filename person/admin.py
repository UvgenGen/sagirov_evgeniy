# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from person.models import Person, Curse
# Register your models here.

class PersonAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']
    
    
class CurseAdmin(admin.ModelAdmin):
    list_display = ['name']
    
    

admin.site.register(Person, PersonAdmin)
admin.site.register(Curse, CurseAdmin)