# -*- coding: utf-8 -*-
from django import forms
from django.forms import ModelForm
from .models import Pregunta, Opcion, Respuesta


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


class RespuestaForm(forms.ModelForm):
    pregunta = None
    user = None

    def __init__(self, pregunta, user, *args, **kwargs):
        super(RespuestaForm, self).__init__(*args, **kwargs)
        self.pregunta = pregunta
        self.fields['option'].label = self.pregunta.text
        self.fields['option'].queryset = self.pregunta.opciones
        self.user = user

    class Meta:
        model = Respuesta
        fields = ('option',)
        exclude = ('question', 'created_date', 'user')

        widgets = {
            'option': forms.Select(attrs={
                'class': 'form-control'
            }),
        }

    def clean_option(self):
        if Respuesta.objects.filter(question=self.pregunta, user=self.user).exists():
            raise forms.ValidationError('Ya contestaste esta pregunta')
        else:
            return self.cleaned_data['option']
