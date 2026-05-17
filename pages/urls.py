from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('about/', views.about, name='about'),
    path('course/<int:pk>/', views.course_detail, name='course_detail'),
    path('contact/', views.contact_view, name='contact'),

    # Вот эти две строчки обязательны:
    path('course/add/', views.course_create, name='course_create'),
    path('course/<int:pk>/edit/', views.course_update, name='course_update'),
]