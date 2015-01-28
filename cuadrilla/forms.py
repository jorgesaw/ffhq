from django import forms
from cuadrilla.models import Bombero


class BomberoForm(forms.ModelForm):

    class Meta:
        model = Bombero
