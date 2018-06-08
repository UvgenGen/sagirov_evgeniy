# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from person.models import person, curse
# Register your models here.

class PersonAdmin(admin.ModelAdmin):
    list_display = ['name', 'email']
    
    
class CurseAdmin(admin.ModelAdmin):
    list_display = ['name']
    
    

admin.site.register(person, PersonAdmin)
admin.site.register(curse, CurseAdmin)