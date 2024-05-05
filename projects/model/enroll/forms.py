from django import forms
from .models import user

class StudentRegistration(forms.ModelForm):
    class Meta:
        model = user
        # fields = ['password', 'name', 'email']
        # fields = '__all__'
        # exclude = ['name',]
        # exclude = ('name')
        fields = ['student_name', 'email', 'password']


class TeacherRegistration(StudentRegistration):
    class Meta(StudentRegistration.Meta):
        fields = ['teacher_name', 'email', 'password']

