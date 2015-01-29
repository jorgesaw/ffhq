# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Bombero',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('nombre', models.CharField(max_length=255, verbose_name='Nombre')),
                ('apellido', models.CharField(max_length=255, verbose_name='Apellido')),
                ('documento', models.CharField(max_length=255, verbose_name='Numero de documento')),
                ('tipo_de_documento', models.CharField(max_length=255, verbose_name='Tipo de documento')),
                ('jerarquia', models.CharField(max_length=255, verbose_name='Jerarquia')),
                ('cargo', models.CharField(max_length=255, verbose_name='Cargo')),
                ('estado', models.CharField(max_length=255, verbose_name='Estado')),
                ('domicilio', models.CharField(max_length=255, verbose_name='Domicilio')),
                ('especialidad', models.CharField(max_length=255, null=True, verbose_name='Especialidad', blank=True)),
                ('ocupacion', models.CharField(max_length=255, null=True, verbose_name='Ocupacion actual', blank=True)),
                ('oficio', models.CharField(max_length=255, null=True, verbose_name='Oficio', blank=True)),
                ('grupo_sanguineo', models.CharField(max_length=255, null=True, verbose_name='Grupo sanguineo', blank=True)),
                ('telefono_celular', models.CharField(max_length=255, null=True, verbose_name='Telefono celular', blank=True)),
                ('telefono_particular', models.CharField(max_length=255, null=True, verbose_name='Telefono particular', blank=True)),
                ('telefono_trabajo', models.CharField(max_length=255, null=True, verbose_name='Telefono del trabajo', blank=True)),
                ('numero_del_hamdy', models.CharField(max_length=255, null=True, verbose_name='numero_del_hamdy', blank=True)),
                ('estado_civil', models.CharField(max_length=255, null=True, verbose_name='Estado civil', blank=True)),
                ('capacitaciones', models.TextField(null=True, verbose_name='Cursos realizados', blank=True)),
                ('estudios', models.TextField(null=True, verbose_name='Estudios realizados', blank=True)),
                ('alergias', models.TextField(null=True, verbose_name='Alergias', blank=True)),
                ('vacunas', models.TextField(null=True, verbose_name='Vacunas', blank=True)),
                ('pencionado', models.BooleanField(default=False, verbose_name='Pencionado')),
                ('carnet_conducir', models.BooleanField(default=False, verbose_name='Carnet de conducir')),
                ('conductor_nautico', models.BooleanField(default=False, verbose_name='Conductor nauticuo')),
                ('chofer', models.BooleanField(default=False, verbose_name='Chofer')),
                ('vencimiento_carnet_conducir', models.DateField(null=True, verbose_name='Vencimiento dwl carnet de conducir', blank=True)),
                ('fecha_de_nacimiento', models.DateField(verbose_name='Fecha de nacimiento')),
                ('fecha_de_ingreso', models.DateField(verbose_name='Fecha de ingreso')),
                ('edad', models.IntegerField(verbose_name='Edad')),
                ('hijos', models.IntegerField(default=0, verbose_name='Hijos')),
                ('antiguedad', models.IntegerField(default=0, verbose_name='Antiguedad')),
                ('numero_de_ioma', models.IntegerField(null=True, verbose_name='Numero de IOMA', blank=True)),
            ],
            options={
            },
            bases=(models.Model,),
        ),
    ]
