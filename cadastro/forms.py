from ast import arg
from dataclasses import fields
import django


from django import forms
from .models import Profissional


class CadastroProfissional(forms.ModelForm):
    class Meta:
        model = Profissional
        fields = "__all__"


    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.fields['usuario'].widget = forms.HiddenInput()