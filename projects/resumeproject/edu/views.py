from django.shortcuts import render

def skills(request):
    context = {"skills" : "active"}
    return render(request, 'edu/skills.html', context)
