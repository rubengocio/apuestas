# -*- coding: utf-8 -*-
from django.apps import apps

from rest_framework import serializers


class ApuestasSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        Opcion = apps.get_model('game', 'Opcion')
        model = Opcion
        fields = ('id', 'question_text', 'question_id', 'text')
