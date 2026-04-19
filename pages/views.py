from django.shortcuts import render, redirect, get_object_or_404
from .forms import FeedbackForm
from .models import Course

def index(request):
    """Главная страница со списком курсов"""
    courses = Course.objects.all()
    return render(request, 'pages/index.html', {
        'title': 'Главная страница',
        'courses': courses
    })

def about(request):
    """Страница О нас"""
    return render(request, 'pages/about.html', {
        'title': 'О нас'
    })

def course_detail(request, pk):
    """Страница конкретного курса"""
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'pages/course_detail.html', {
        'course': course
    })

def contact_view(request):
    """Страница обратной связи (ДЗ-8)"""
    if request.method == 'POST':
        form = FeedbackForm(request.POST)
        if form.is_valid():
            print("\n" + "="*30)
            print("ОТЛАДКА: ФОРМА ПОЛУЧЕНА")
            print(f"Тема: {form.cleaned_data.get('subject')}")
            print(f"Email: {form.cleaned_data.get('email')}")
            print(f"Сообщение: {form.cleaned_data.get('text')}")
            print("="*30 + "\n")
            
            return redirect('home')
    else:
        form = FeedbackForm()
    
    return render(request, 'pages/contact.html', {
        'title': 'Обратная связь',
        'form': form
    })