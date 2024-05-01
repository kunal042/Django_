from django.shortcuts import render
from .forms import StudentRegistration



def student(request):
    if request.method == "POST":
        fm = StudentRegistration(request.POST)
        if fm.is_valid:
            nm = fm.cleaned_data['name']
            em = fm.cleaned_data['email']

            print(f"Name : {nm}")
            print(f"Name : {em}")

            print("This is post method")
    else:
        fm = StudentRegistration()
        print("This get method")
    

    return render(request, 'enroll/index.html', {'forms':fm} )
