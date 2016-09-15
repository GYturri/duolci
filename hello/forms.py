from django import forms
from django.forms import ModelForm

from .models import Caidos

class CaidoForm(forms.ModelForm):
	class Meta:
		model = Caidos
		exclude = ("id","reg",)