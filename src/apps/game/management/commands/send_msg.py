# -*- coding: utf-8 -*-
from django.core.management.base import BaseCommand
from django.core import mail


class Command(BaseCommand):

    def handle(self, *args, **options):
        connection = mail.get_connection()
        import ipdb; ipdb.set_trace()
        connection.open()

        mail0 = mail.EmailMessage(
            'Asunto 0',
            'Cuerpo del email 0',
            'eldwarf1@gmail.com',
            ['rubengocio@gmail.com'],
            connection=connection
        )
        mail0.send()

        mail1 = mail.EmailMessage(
            'Asunto 1',
            'Cuerpo del email 1',
            'eldwarf1@gmail.com',
            ['rgocio@mobydigital.com'],
            connection=connection
        )
        mail1.send()
        #connection.send_messages([mail0,mail1])
        connection.close()
