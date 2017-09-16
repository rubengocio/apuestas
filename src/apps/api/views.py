# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import User
#from django.shortcuts import render
from django.apps import apps

from rest_framework import viewsets
from rest_framework import permissions, authtoken
from rest_framework.decorators import api_view
from rest_framework.response import Response

#from apps.game.models import Opcion
from .serializers import ApuestasSerializer


class ApuestasViewSet(viewsets.ModelViewSet):
    Opcion = apps.get_model('game', 'Opcion')
    queryset = Opcion.objects.all()
    serializer_class = ApuestasSerializer
    permission_classes = (permissions.IsAuthenticated,)


@api_view(['POST'])
def registrar_apuesta(request):
    if request.method == 'POST':
        usuario_id = request.POST.get('usuario_id', 0)
        respuesta_id = request.POST.get('respuesta_id', 0)
        Opcion = apps.get_model('game', 'Opcion')
        Respuesta = apps.get_model('game', 'Respuesta')
        #user = User.objects.get(pk=usuario_id)
        opcion = Opcion.objects.get(pk=respuesta_id)
        apuesta = Apuestas(
            option=opcion,
            user=request.user
        )
        apuesta.save()
        return Response({
            'status': 'ok'
        })
    return Response({
        "status": "error",
        "response": ""
    })


"""
method = "POST"
handler = urllib2.HTTPHandler()
opener = urllib2.build_opener(handler)
data = urllib.urlencode({'usuario_id':'', respuesta_id
request = urllib2.Request(url, data=data)
request.add_header("Content-Type",'application/json')
request.get_method = lambda: method
try:
    connection = opener.open(request)
except urllib2.HTTPError,e:
    connection = e
if connection.code == 200:
    data = connection.read()
else:
    pass
"""
