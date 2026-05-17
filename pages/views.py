from django.shortcuts import render, redirect, get_object_or_404
from .models import Course
from .forms import CourseForm

def index(request):
    """Главная страница со списком всех курсов"""
    courses = Course.objects.all()
    return render(request, 'pages/index.html', {
        'title': 'Главная | M School',
        'welcome_message': 'Добро пожаловать в M School!',
        'courses': courses
    })

def course_detail(request, pk):
    """Детальная страница конкретного курса"""
    course = get_object_or_404(Course, pk=pk)
    return render(request, 'pages/course_detail.html', {
        'course': course,
        'title': course.title
    })

def course_create(request):
    """Создание нового языкового курса через ModelForm"""
    if request.method == 'POST':
        form = CourseForm(request.POST)
        if form.is_valid():
            new_course = form.save()
            return redirect('course_detail', pk=new_course.pk)
    else:
        form = CourseForm()
        
    return render(request, 'pages/course_form.html', {
        'form': form, 
        'title': 'Добавление нового курса'
    })

def course_update(request, pk):
    """Редактирование существующего курса с защитой от дублирования"""
    course = get_object_or_404(Course, pk=pk)
    
    if request.method == 'POST':
        form = CourseForm(request.POST, instance=course)
        if form.is_valid():
            form.save()
            return redirect('course_detail', pk=course.pk)
    else:
        form = CourseForm(instance=course)
        
    return render(request, 'pages/course_form.html', {
        'form': form, 
        'title': f'Редактирование курса: {course.title}'
    })

def about(request):
    """Страница 'О нас' (заглушка)"""
    return render(request, 'pages/about.html', {'title': 'О нас | M School'})

def contact_view(request):
    """Страница 'Контакты' (заглушка)"""
    return render(request, 'pages/contact.html', {'title': 'Контакты | M School'})