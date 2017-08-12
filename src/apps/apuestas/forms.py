# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from .models import Pregunta, Opcion


class PreguntaForm(forms.ModelForm):

    def __init__(self, *args, **kwargs):
        super(PreguntaForm, self).__init__(*args, **kwargs)

    class Meta:
        model = Pregunta
        fields = ('text', 'due_date')
        exclude = ('author', 'created_date', 'updated_date')

        widgets = {
            'text': forms.TextInput(attrs={
                'placeholder': 'Ingrese la pregunta.',
                'class': 'form-control'
            }),
            'due_date': forms.TextInput(attrs={
                'class': 'form-control'
            }),
        }

    def save(self, commit=True):
        return super(PreguntaForm, self).save(commit=commit)
