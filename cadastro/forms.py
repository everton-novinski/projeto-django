from dataclasses import fields
import django


from django import forms
from .models import Profissional


class CadastroProfissional(forms.ModelForm):
    class Meta:
        model = Profissional
        fields = "__all__"


