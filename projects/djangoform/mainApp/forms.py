from django import forms


class StudentRegistration(forms.Form):
    name = forms.CharField(
        label='Your Name', 
        label_suffix=" ", 
        initial='sonma', 
        required=False, 
        help_text="limit 30 char")
    email = forms.EmailField()
    first_name = forms.CharField()
    mobile = forms.IntegerField()

    key = forms.CharField(widget=forms.HiddenInput())
