# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class Pregunta(models.Model):
    text = models.CharField(max_length=300)
    author = models.ForeignKey(User)
    created_date = models.DateTimeField('Fecha de creacion:', auto_now_add=True)
    updated_date = models.DateTimeField('Fecha de actualizacion:', auto_now=True)
    due_date = models.DateTimeField('Fecha limite')

    def __unicode__(self):
        return "%s" % texto

    @property
    def opciones(self):
        return Opcion.objects.filter(quetion=self)

class Opcion(models.Model):
    question = models.ForeignKey(Pregunta, on_delete=models.CASCADE)
    text = models.CharField(max_length=250)
    author = models.ForeignKey(User)
    created_date = models.DateTimeField('Fecha de creacion:',auto_now_add=True)
    updated_date = models.DateTimeField('Fecha de actualizacion:',auto_now=True)

    class Meta:
        unique_together = ('question','text')

    def __unicode__(self):
        return "%s" % text

class Respuesta(models.Model):
    user = models.ForeignKey(User)
    option = models.ForeignKey(Opcion)
    created_date = models.DateTimeField('Fecha de creacion:',auto_now_add=True)

    class Meta:
        unique_together = ('user','option')
