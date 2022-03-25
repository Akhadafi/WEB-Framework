from django import forms
from django.forms import fields

from .models import Artikel


class ArtikelForm(forms.ModelForm):
    class Meta:
        model = Artikel
        fields = [
            "judul",
            "isi",
            "penulis",
        ]
