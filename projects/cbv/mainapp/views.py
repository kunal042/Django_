from django.shortcuts import render, HttpResponse
from django.views import View
from .forms import ContactForm

# Create your views here.

def myviews(request):
    return HttpResponse("<h2> This is function based views </h2>")


class MyView(View):
    name = "kunal"

    def get(self, request ):
        
        # return HttpResponse("<h2> This is Class based views -- GET </h2>")
        return HttpResponse(self.name)


class MyViewChild(MyView):
    def get(self, request):
        return HttpResponse(self.name)
    

def home(request):
    return render(request, 'mainapp/home.html')


class Homeclass(View):
    def get(self, request):
        return render(request, 'mainapp/home.html')
    


#####################################################


def aboutfun(request):
    context = {
        "msg" : "Welcome to function based views"
    }
    return render(request, "mainapp/about.html", context)


class AboutClass(View):
    def get(self, request):
        context = {
            "msg" : "Welcome to Class based views"
        }
        return render(request, "mainapp/about.html", context)
    


#############################################


def contact(request):
    if request.method == "POST":
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            return HttpResponse("Thank you ! form submitted!!")
        
    else :
        form = ContactForm()

    return render(request, 'mainapp/contact.html', {'form':form})


class ContactClass(View):
    def get(self, request):
        form = ContactForm()
        return render(request, 'mainapp/contact.html', {'form':form})
    
    def post(self,request):
        form = ContactForm(request.POST)
        if form.is_valid():
            print(form.cleaned_data['name'])
            return HttpResponse("Thank you ! form submitted!!")
        

#################################################


def news(request,templates_name):
    templates_name = templates_name
    context = {
        'info' : 'CBI enquiry why kunal show earn less money!!'
    }

    return render(request, templates_name, context)



class NewsClass(View):
    templates_name = ''
    def get(self, request):
        
        context = {
        'info' : 'CBI enquiry why kunal show earn less money!!'
    }

        return render(request, self.templates_name, context)
