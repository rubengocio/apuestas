# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import Pregunta, Opcion

def add_simbol_text(modeladmin,request,queryset):
	for q in queryset:
		q.text = q.text + '?'
		q.save()

add_simbol_text.short_description = 'Agregar simbolo ?'

class OpcionHeadInLine(admin.TabularInline):
    model = Opcion
    extra = 1

# Register your models here.
class PreguntaAdmin(admin.ModelAdmin):
	list_display = ('id','text','author',)
	search_fields = ('text','author__username')
	list_filter = ('author__username',)
	actions = [add_simbol_text,]
	inlines = [OpcionHeadInLine,]


admin.site.register(Pregunta, PreguntaAdmin)
admin.site.register(Opcion)