from django import forms
from .models import user

class registration(forms.ModelForm):
    class meta:
        model = user
        fields = ['name', 'email', 'password']
