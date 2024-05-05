from django import forms
from .models import user

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = user
        fields = ['name', 'email', 'password']
