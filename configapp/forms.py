from django import forms
from .models import AutoSalon, Brend, Car

class AutoSalonForm(forms.ModelForm):
    class Meta:
        model = AutoSalon
        fields = ['title', 'context', 'email', 'phone', 'address', 'img']


class BrendForm(forms.ModelForm):
    class Meta:
        model = Brend
        fields = ['title', 'context']


class CarForm(forms.ModelForm):
    class Meta:
        model = Car
        fields = ['salon', 'brend', 'model_name', 'price', 'year', 'color', 'img']
