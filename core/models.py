# -*- coding: utf-8 -*-

from django.db import models
from model_utils import Choices
from model_utils.fields import StatusField


class Tracked(models.Model):
    created = models.DateField(auto_now_add=True, editable=True, null=True, verbose_name=u'fecha de creación')
    modified = models.DateField(auto_now=True, editable=True, null=True, verbose_name=u'fecha de modificación')

    class Meta:
        abstract = True


class Category(Tracked):
    name = models.CharField(max_length=150, verbose_name=u'rubro')

    def __unicode__(self):
        return self.name

    class Meta:
        verbose_name = u'rubro'
        verbose_name_plural = u'rubros'


class Client(Tracked):
    contact = models.CharField(max_length=150, verbose_name=u'nombre')
    company = models.CharField(max_length=150, verbose_name=u'razon social')
    address = models.CharField(max_length=200, verbose_name=u'dirección')
    cuit = models.CharField(max_length=100, verbose_name=u'cuit')
    category = models.ForeignKey(Category, null=True, blank=True, verbose_name=u'rubro')

    def __unicode__(self):
        return self.company

    class Meta:
        verbose_name = u'cliente'
        verbose_name_plural = u'clientes'


class ServiceType(Tracked):
    name = models.CharField(max_length=150, verbose_name=u'nombre')
    tag = models.CharField(blank=True, max_length=150, verbose_name=u'tag')

    def __unicode__(self):
        return '%s [%s]' % (self.name, self.tag)

    def save(self, *args, **kwargs):
        self.tag = self.tag or self._tag()
        super(ServiceType, self).save(*args, **kwargs)

    def _tag(self):
        words = self.name.split()
        return ''.join(map(lambda w: w[0] if len(w) > 2 else '', words)).upper()

    class Meta:
        verbose_name = u'tipo de servico'
        verbose_name_plural = u'tipos de servico'


class Service(Tracked):
    KINDS = Choices(('simple', 'Simple'), ('month', 'Mensual'), ('anual', 'Anual'))

    category = models.ForeignKey(ServiceType, verbose_name=u'tipo de servicio')
    name = models.CharField(max_length=150, verbose_name=u'nombre')
    kind = models.CharField(choices=KINDS, default=KINDS.simple, max_length=20, verbose_name=u'frecuencia')

    def __unicode__(self):
        return '[%s] - %s' % (self.category.tag, self.name)

    class Meta:
        verbose_name = u'servico'
        verbose_name_plural = u'servicios'


class Job(Tracked):
    STATUS = Choices(('budget', 'Presupuestado'), ('progress', 'Aprovado'), ('finished', 'Finalizado'), ('canceled', 'No Aprobado'))
    status = StatusField(verbose_name=u'estado')

    client = models.ForeignKey(Client, verbose_name=u'cliente')
    service = models.ForeignKey(Service, verbose_name=u'servicio')
    price = models.FloatField(verbose_name=u'precio')

    comments = models.TextField(null=True, blank=True, verbose_name=u'comentarios')
    attachment = models.FileField(null=True, blank=True, upload_to='./work', verbose_name=u'presupuesto')

    def __unicode__(self):
        return '{} - {}'.format(self.service, self.client)

    class Meta:
        abstract = True


class SimpleJob(Job):
    advance = models.FloatField(null=True, blank=True, verbose_name=u'monto de adelanto')
    deadline = models.DateField(null=True, blank=True, verbose_name=u'fecha de entrega')

    class Meta:
        verbose_name = u'trabajo'
        verbose_name_plural = u'trabajos'


class RegularJob(Job):
    start_date = models.DateField(null=True, blank=True, verbose_name=u'Inicio del trabajo')
    end_date = models.DateField(null=True, blank=True, verbose_name=u'Fin del Trabajo')

    class Meta:
        verbose_name = u'trabajo regulares'
        verbose_name_plural = u'trabajos regulares'
