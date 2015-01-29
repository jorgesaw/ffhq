from django import forms
from cuadrilla import choices
from cuadrilla.models import Bombero
from django.utils.translation import ugettext_lazy as _
from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Field, Row, Column


class BomberoForm(forms.ModelForm):

    tipo_de_documento = forms.CharField(
        label="",
        widget=forms.Select(choices=choices.TIPO_DOCUMENTO_ES_AR,
                            attrs={'class': 'browser-default'}
                            )
    )

    def __init__(self, *args, **kwargs):
        super(BomberoForm, self).__init__(*args, **kwargs)
        self.helper = FormHelper(self)
        self.helper.form_class = 'col s12'
        self.helper.layout = Layout(
            Row(
                Column(
                    Field('nombre'),
                    css_class='col s6'
                ),
                Column(
                    Field('apellido'),
                    css_class='col s6'
                )
            ),
            Row(
                Column(
                    Field('documento'),
                    css_class='col s6'
                ),
                Column(
                    Field('tipo_de_documento'),
                    css_class='col s6'
                )
            )
        )

    class Meta:
        model = Bombero
        fields = (
            'nombre',
            'apellido',
            'documento',
            'tipo_de_documento',
            'jerarquia',
            'cargo',
            'estado',
            'fecha_de_nacimiento',
            'edad',
            'fecha_de_ingreso',
            'antiguedad',
            'numero_de_ioma',
            'grupo_sanguineo',
            'domicilio',
            'pencionado',
            'telefono_celular',
            'telefono_particular',
            'telefono_trabajo',
            'numero_del_hamdy',
            'especialidad',
            'capacitaciones',
            'estudios',
            'ocupacion',
            'hijos',
            'estado_civil',
            'alergias',
            'vacunas',
            'oficio',
            'carnet_conducir',
            'chofer',
            'vencimiento_carnet_conducir',
            'conductor_nautico'
        )
