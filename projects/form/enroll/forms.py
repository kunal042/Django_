from django import forms


class StudentRegistration(forms.Form):
    name = forms.CharField(min_length=5, max_length=40, strip=False,
                           empty_value='Kunal', error_messages={'requied': 'Enter your Name'})
    roll = forms.IntegerField(min_value=5, max_value=40)

    price = forms.DecimalField(min_value=5, max_value=40, decimal_places=1)
    rate = forms.FloatField(min_value=5, max_value=40, )

    comment = forms.SlugField()
    email = forms.EmailField(min_length=5, max_length=40)
    website = forms.URLField(min_length=5, max_length=50)
    password = forms.CharField(
        min_length=5, max_length=50, widget=forms.PasswordInput)
    description = forms.CharField(widget=forms.Textarea)
    feedback = forms.CharField(min_length=5, max_length=50, widget=forms.TextInput(
        attrs={'class': 'somecss1 somecss2', 'id':'uniquied'}))
    note = forms.CharField(widget=forms.Textarea(attrs={'row':3, 'col':50}))

    agree = forms.BooleanField(label_suffix="", label='I Agree', error_messages={
                               'requied': 'Accept the agree button'})
