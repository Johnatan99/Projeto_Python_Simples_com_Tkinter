from django.forms import ModelForm
from app.models import Carros
from django import forms
 
class CarrosForm(forms.Form):
    class Meta:
        model = Carros
        fields = "__all__"