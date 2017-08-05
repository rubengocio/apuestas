# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import PreguntaForm
from .models import Pregunta

# Create your views here.
def index(request):
    form = PreguntaForm()

    if request.method == 'POST':
        form = PreguntaForm(data=request.POST)
        if form.is_valid():
            pregunta = form.save(commit=False)
            pregunta.author = request.user
            pregunta.save()

    template = loader.get_template('index.html')
    pregunta_list = Pregunta.objects.all()
    context = {
        'username' : request.user.username,
        'form' : form,
        'pregunta_list' : pregunta_list
    }
    return HttpResponse(template.render(context,request))
