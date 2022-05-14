from django import forms
from .models import *


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'}),
            'last_name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
        }


class SearchPerson(forms.ModelForm):
    class Meta:
        model = Contact
        fields = ['first_name']
        widgets = {
            'first_name': forms.TextInput(attrs={'class': 'form-control'})
        }