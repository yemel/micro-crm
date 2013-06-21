# -*- coding: utf-8 -*-
import datetime

from django.core.management.base import BaseCommand
from django.db.transaction import commit_on_success
from django.contrib.auth.models import User

from core.models import Category, Client, ServiceType, Service, SimpleJob, RegularJob

deadline = lambda days: datetime.date.today() + datetime.timedelta(days=days)


class Command(BaseCommand):
    help = 'Creates initial data'

    @commit_on_success
    def handle(self, *args, **options):

        # Create Admin
        u = User.objects.create(username="yemel", first_name="Yemel", last_name="Jardi", is_staff=True, is_superuser=True)
        u.set_password('1234')
        u.save()

        # Create Categories
        r1 = Category.objects.create(name='Industrial')
        r2 = Category.objects.create(name='Gastronomía')
        r3 = Category.objects.create(name='Chatarrera')

        dclient = {'address': 'Libertador 1234, Buenos Aires', 'cuit': '1-82742454-2'}

        c1 = Client.objects.create(contact='Ruben Martinez', company="Marco Polo SA", category=r1, **dclient)
        c2 = Client.objects.create(contact='Gonzalo Perez', company="Clorox SA", category=r1, **dclient)
        c3 = Client.objects.create(contact='Mariano Diaz', company="Los Tachitos SA", category=r2, **dclient)
        c4 = Client.objects.create(contact='Daniel Souza', company="Noscowe SA", category=r2, **dclient)
        c5 = Client.objects.create(contact='Benito Lopez', company="Lima SA", category=r3, **dclient)

        t = ServiceType.objects.create(name=u'Documentación Provincial')
        s01 = Service.objects.create(category=t, name=u'Categorización', kind=Service.KINDS.simple)
        s02 = Service.objects.create(category=t, name=u'Recategorizacion', kind=Service.KINDS.simple)
        s03 = Service.objects.create(category=t, name=u'Factibilidad', kind=Service.KINDS.simple)
        s04 = Service.objects.create(category=t, name=u'Estudio de impacto ambiental', kind=Service.KINDS.simple)
        s05 = Service.objects.create(category=t, name=u'Auditoria ambiental de renovación de impacto ambiental', kind=Service.KINDS.simple)
        s06 = Service.objects.create(category=t, name=u'Declaracion Jurada de Residuos especiales', kind=Service.KINDS.anual)

        t = ServiceType.objects.create(name=u'Documentacion de compresores y calderas')
        s07 = Service.objects.create(category=t, name=u'Habilitacion de aparatos sometidos a presion sin fuego', kind=Service.KINDS.simple)
        s08 = Service.objects.create(category=t, name=u'Habilitacion de aparatos sometidos a presion con fuego', kind=Service.KINDS.simple)
        s09 = Service.objects.create(category=t, name=u'Extensión de vida util de aparatos sometidos a presion con fuego', kind=Service.KINDS.simple)
        s10 = Service.objects.create(category=t, name=u'Extensión de vida util de aparatos sometidos a presion sin fuego', kind=Service.KINDS.simple)
        s11 = Service.objects.create(category=t, name=u'Medicion de espesores de aparatos sometidos a presion con fuego', kind=Service.KINDS.anual)
        s12 = Service.objects.create(category=t, name=u'Medicion de espesores de aparatos sometidos a presion sin fuego', kind=Service.KINDS.anual)

        t = ServiceType.objects.create(name=u'Documentacion de efluentes gaseosos')
        s13 = Service.objects.create(category=t, name=u'Medicion y solicitud de Permiso de emision a la atmosfera', kind=Service.KINDS.simple)
        s14 = Service.objects.create(category=t, name=u'Monitoreo de emisiones gaseososas', kind=Service.KINDS.anual)

        t = ServiceType.objects.create(name=u'Documentacion municipal')
        s15 = Service.objects.create(category=t, name=u'Habilitacion de industria', kind=Service.KINDS.simple)
        s16 = Service.objects.create(category=t, name=u'Actualizacion de habilitacion de industria', kind=Service.KINDS.simple)
        s17 = Service.objects.create(category=t, name=u'Habilitacion comercial', kind=Service.KINDS.simple)
        s18 = Service.objects.create(category=t, name=u'Baja de habilitacion comercial', kind=Service.KINDS.simple)
        s19 = Service.objects.create(category=t, name=u'Plano de obra', kind=Service.KINDS.simple)

        t = ServiceType.objects.create(name=u'Documentacion efluentes liquidos')
        s20 = Service.objects.create(category=t, name=u'Declaracion Jurada de E. liquidos', kind=Service.KINDS.anual)
        s21 = Service.objects.create(category=t, name=u'Plano Sanitario', kind=Service.KINDS.simple)
        s22 = Service.objects.create(category=t, name=u'Muestreo de vertidos', kind=Service.KINDS.simple)

        t = ServiceType.objects.create(name=u'Documentacion Nacional')
        s23 = Service.objects.create(category=t, name=u'Servicio de higiene y seguridad en el trabajo', kind=Service.KINDS.month)
        s24 = Service.objects.create(category=t, name=u'Estudio de carga de fuego', kind=Service.KINDS.simple)
        s25 = Service.objects.create(category=t, name=u'Mediciones de puesta a tierra', kind=Service.KINDS.simple)
        s26 = Service.objects.create(category=t, name=u'Mediciones ambientales internas', kind=Service.KINDS.simple)
        s27 = Service.objects.create(category=t, name=u'Medicion de ruidos externos', kind=Service.KINDS.simple)
        s28 = Service.objects.create(category=t, name=u'Solicitud de clave unico de empradronameinto territorial (CURT)', kind=Service.KINDS.simple)
        s29 = Service.objects.create(category=t, name=u'Seguro ambiental', kind=Service.KINDS.simple)
        s30 = Service.objects.create(category=t, name=u'Solicitud de eximicion del seguro ambiental', kind=Service.KINDS.simple)
        s31 = Service.objects.create(category=t, name=u'Capacitaciones en seguridad e higiene', kind=Service.KINDS.simple)

        budget = SimpleJob.STATUS.budget
        SimpleJob.objects.create(client=c1, service=s01, status=budget, price=1500, advance=500, deadline=deadline(20))
        SimpleJob.objects.create(client=c1, service=s02, status=budget, price=1500, advance=500, deadline=deadline(20))
        SimpleJob.objects.create(client=c2, service=s03, status=budget, price=1500, advance=500, deadline=deadline(20))
        SimpleJob.objects.create(client=c3, service=s04, status=budget, price=1500, advance=500, deadline=deadline(20))
        SimpleJob.objects.create(client=c4, service=s05, status=budget, price=1500, advance=500, deadline=deadline(20))
        SimpleJob.objects.create(client=c5, service=s08, status=budget, price=1500, advance=500, deadline=deadline(20))


        RegularJob.objects.create(client=c1, service=s20, status=budget, price=1500)
        RegularJob.objects.create(client=c1, service=s20, status=budget, price=1500)
        RegularJob.objects.create(client=c2, service=s23, status=budget, price=1500)
        RegularJob.objects.create(client=c3, service=s06, status=budget, price=1500)
        RegularJob.objects.create(client=c4, service=s06, status=budget, price=1500)
        RegularJob.objects.create(client=c5, service=s06, status=budget, price=1500)
