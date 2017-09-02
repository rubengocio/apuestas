# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.contrib.auth.models import Group
from django.http import HttpResponse
from django.shortcuts import render
from django.template import loader
from django.contrib.auth.forms import UserCreationForm
from functions import json_response
# Create your views here.


def register_user(request):
    template = loader.get_template('registration/register.html')
    form = UserCreationForm()

    if request.method == 'POST':
        form = UserCreationForm(data=request.POST)

        if form.is_valid():
            user = form.save(commit=False)
            user.is_active = True
            grupo_jugador = Group.objects.get(name='Jugador')
            user.save()
            user.groups.add(grupo_jugador)
            response = json_response().response_ok()
        else:
            response = json_response().response_error_form(form)
        return response
    context = {
        'form': form
    }
    return HttpResponse(template.render(context, request))
