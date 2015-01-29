from django.db import models
from django.utils.translation import ugettext as _


class Bombero(models.Model):
    nombre = models.CharField(
        max_length=255,
        verbose_name=_('Nombre'))
    apellido = models.CharField(
        max_length=255,
        verbose_name=_('Apellido'))
    documento = models.CharField(
        max_length=255,
        verbose_name=_('Numero de documento'))
    tipo_de_documento = models.CharField(
        max_length=255,
        verbose_name=_('Tipo de documento'))
    jerarquia = models.CharField(
        max_length=255,
        verbose_name=_('Jerarquia'))
    cargo = models.CharField(
        max_length=255,
        verbose_name=_('Cargo'))
    estado = models.CharField(
        max_length=255,
        verbose_name=_('Estado'))
    domicilio = models.CharField(
        max_length=255,
        verbose_name=_('Domicilio'))
    especialidad = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        verbose_name=_('Especialidad'))
    ocupacion = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        verbose_name=_('Ocupacion actual'))
    oficio = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        verbose_name=_('Oficio'))
    grupo_sanguineo = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        verbose_name=_('Grupo sanguineo'))
    telefono_celular = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        verbose_name=_('Telefono celular'))
    telefono_particular = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        verbose_name=_('Telefono particular'))
    telefono_trabajo = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        verbose_name=_('Telefono del trabajo'))
    numero_del_hamdy = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        verbose_name=_('Numero del Hamdy'))
    estado_civil = models.CharField(
        null=True,
        blank=True,
        max_length=255,
        verbose_name=_('Estado civil'))
    capacitaciones = models.TextField(
        null=True,
        blank=True,
        verbose_name=_('Cursos realizados'))
    estudios = models.TextField(
        null=True,
        blank=True,
        verbose_name=_('Estudios realizados'))
    alergias = models.TextField(
        null=True,
        blank=True,
        verbose_name=_('Alergias'))
    vacunas = models.TextField(
        null=True,
        blank=True,
        verbose_name=_('Vacunas'))
    pencionado = models.BooleanField(
        default=False,
        verbose_name=_('Pencionado')
    )
    carnet_conducir = models.BooleanField(
        default=False,
        verbose_name=_('Carnet de conducir')
    )
    conductor_nautico = models.BooleanField(
        default=False,
        verbose_name=_('Conductor nauticuo')
    )
    chofer = models.BooleanField(
        default=False,
        verbose_name=_('Chofer')
    )
    vencimiento_carnet_conducir = models.DateField(
        null=True,
        blank=True,
        verbose_name=_('Vencimiento dwl carnet de conducir')
    )
    fecha_de_nacimiento = models.DateField(
        verbose_name=_('Fecha de nacimiento')
    )
    fecha_de_ingreso = models.DateField(
        verbose_name=_('Fecha de ingreso')
    )
    edad = models.IntegerField(
        verbose_name=_('Edad')
    )
    hijos = models.IntegerField(
        default=0,
        verbose_name=_('Hijos')
    )
    antiguedad = models.IntegerField(
        default=0,
        verbose_name=_('Antiguedad')
    )
    numero_de_ioma = models.IntegerField(
        null=True,
        blank=True,
        verbose_name=_('Numero de IOMA')
    )
