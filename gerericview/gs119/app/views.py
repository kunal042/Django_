from django.shortcuts import render
from .forms import ContactForm, FeedbackForm
from django.views.generic.edit import FormView
from django.views.generic.base import TemplateView

# Create your views here.

class ContactFormView(FormView):
    template_name = 'app/contact.html'
    form_class = FeedbackForm
    success_url = '/thankyou/'
    initial = {"your_name": "kunal"}

    def form_valid(self, form):
        print(form)
        print(form.cleaned_data['your_name'])
        print(form.cleaned_data['your_email'])
        print(form.cleaned_data['msg'])
        return super().form_valid(form)
    


class ThanksTemplatesView(TemplateView):
    template_name = 'app/thankyou.html'