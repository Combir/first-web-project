from django.shortcuts import render

def index(request):
    context = {
        'title': 'Главная — M School',
        'welcome_message': 'Добро пожаловать в школу иностранных языков!',
    }
    return render(request, 'pages/index.html', context)

def about(request):
    context = {
        'title': 'О школе — M School',
    }
    return render(request, 'pages/about.html', context)