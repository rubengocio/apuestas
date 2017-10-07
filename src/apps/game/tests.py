# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.test import TestCase, Client
from .models import Pregunta, Opcion
from datetime import datetime
from django.contrib.auth.models import User



class abm_apuestas(TestCase):

    def setUp(self):
        self.user = User(username='ruben_gocio@hotmail.com')
        self.user.set_password('ABCabc123')
        self.user.save()

    def test_crear_pregunta(self):
        pregunta = Pregunta(
            text='¿Llueve mañana?',
            author = self.user,
            due_date = datetime.now()
        )
        pregunta.save()


    def test_crear_opciones(self):
        pregunta = Pregunta(
            text='¿Llueve mañana?',
            author=self.user,
            due_date=datetime.now()
        )
        pregunta.save()
        opcion1 = Opcion(
            question = pregunta,
            text = 'Opcion 1',
            author = self.user
        )
        opcion2 = Opcion(
            question=pregunta,
            text='Opcion 2',
            author=self.user
        )

    def test_home(self):
        client = Client()
        response = client.get('/kkkkk')
        print(response.status_code)

    def test_login_post_password_error(self):
        client = Client()
        response = client.post(
            '/accounts/login/',
            {
                'username':'ruben_gocio@hotmail.com',
                'password':''
            }
        )
        self.assertFormError(response, 'form', 'password', 'This field is required.')

    def test_login_post_ok(self):
        from django.contrib.auth.forms import UserCreationForm
        form = UserCreationForm(data={'username':'ruben_gocio@hotmail.com','password1':'123456ABC','password2':'123456ABC'})
        self.assertTrue(form.is_valid())


    def test_login_post_ok2(self):
        client = Client()
        response = client.post(
            '/accounts/login/',
            {
                'username':'ruben_gocio@hotmail.com',
                'password':'ABCabc123'
            }
        )
        #validator = False
        #if response.status_code = 302:
        #    validator = True
        #self.assertTrue(validator)
        self.assertRedirects(response,'/apuestas/')


class jugar_apuestas(TestCase):

    def test_listar_usuarios(self):
        print(User.objects.all())
