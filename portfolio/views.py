from django.shortcuts import render
from .models import Project

def home(request):
    temp = 'My_home_page'
    projects = Project.objects.all()
    return render(request, 'portfolio/home.html', {'temp': temp, 'projects': projects})

def home_vba(request):
    return render(request, 'portfolio/vba.html')

def my_django(request):
    return render(request, 'portfolio/my_django.html')

def syst(request):
    return render(request, 'portfolio/syst.html')
