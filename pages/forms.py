from django import forms
from .models import Course

class CourseForm(forms.ModelForm):
    class Meta:
        model = Course
        fields = ['title', 'description', 'level', 'duration_months', 'price']
               
        widgets = {
            'title': forms.TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Например: Английский для IT-специалистов'
            }),
            'description': forms.Textarea(attrs={
                'class': 'form-control',
                'rows': 4,
                'placeholder': 'Подробное описание программы курса...'
            }),
            'level': forms.Select(attrs={
                'class': 'form-select'
            }),
            'duration_months': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '1'
            }),
            'price': forms.NumberInput(attrs={
                'class': 'form-control',
                'min': '0'
            }),
        }