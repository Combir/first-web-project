from django.shortcuts import render
from .models import Course

def index(request):
    courses = Course.objects.all()
    
    context = {
        'title': 'Главная — M School',
        'welcome_message': 'Добро пожаловать в школу иностранных языков!',
        'courses': courses,
    }
    return render(request, 'pages/index.html', context)

def about(request):
    context = {
        'title': 'О школе — M School',
    }
    return render(request, 'pages/about.html', context)