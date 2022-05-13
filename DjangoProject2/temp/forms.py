from django import forms
from .models import Contact


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contact
        fields = '__all__'
        widgets = {
            'name': forms.TextInput(attrs={'class': 'form-control'}),
            'email': forms.EmailInput(attrs={'class': 'form-control'}),
            'choice': forms.Select(attrs={'class': 'form-control'}),
            'text': forms.Textarea(attrs={'class': 'form-control'})
        }