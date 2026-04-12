from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('course/<int:pk>/', views.course_detail, name='course_detail'),
]