# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
from .forms import PreguntaForm, RespuestaForm
from .models import Pregunta
from django.views import View
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

# Create your views here.
@login_required
def apuestas_list(request):
    form = PreguntaForm()

    template = loader.get_template('apuestas_list.html')
    pregunta_list = Pregunta.objects.all()
    context = {
        'username' : request.user.username,
        'form' : form,
        'pregunta_list' : pregunta_list
    }
    return HttpResponse(template.render(context,request))


class PreguntaView(LoginRequiredMixin, View):
    form = PreguntaForm()
    template_name = "pregunta_form.html"

    def get(self, request, *args, **kwargs):
        id_pregunta = self.kwargs['id_pregunta']
        prg = Pregunta.objects.get(pk=id_pregunta)
        form = PreguntaForm(instance=prg)
        context = {
            'form': form
        }
        return render(request, self.template_name, context)

    def post(self, request, *args, **kwargs):
        id_pregunta = self.kwargs['id_pregunta']
        prg = Pregunta.objects.get(pk=id_pregunta)
        form = PreguntaForm(data=request.POST, instance=prg)
        if form.is_valid():
            prg = form.save(commit=False)
            prg.save()
        context = {
            'form': form
        }
        return render(request, self.template_name, context)


@login_required
def respuesta(request, id_pregunta):
    template = loader.get_template('respuesta.html')
    pregunta = Pregunta.objects.get(pk=id_pregunta)
    form = RespuestaForm(pregunta, request.user)

    if request.method == 'POST':
        form = RespuestaForm(pregunta, request.user, data=request.POST)
        if form.is_valid():
            respuesta = form.save(commit=False)
            respuesta.user = request.user
            respuesta.save()

    context = {
        'form': form,
        'pregunta': pregunta
    }
    return HttpResponse(template.render(context,request))
