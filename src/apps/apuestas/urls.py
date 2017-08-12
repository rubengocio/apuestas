from django.conf.urls import url
from django.contrib import admin
from .views import index, PreguntaView

urlpatterns = [
    url(r'^$', index, name='apuestas_index'),
    url(r'^(?P<id_pregunta>\d+)/$', PreguntaView.as_view())
]
