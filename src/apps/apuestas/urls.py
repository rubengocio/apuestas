from django.conf.urls import url
from django.contrib import admin
from .views import apuestas_list, PreguntaView

urlpatterns = [
    url(r'^$', apuestas_list, name='apuestas_list'),
    url(r'^(?P<id_pregunta>\d+)/$', PreguntaView.as_view())
]
