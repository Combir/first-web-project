from django import forms

class FeedbackForm(forms.Form):
    subject = forms.CharField(
        label='Тема письма',
        max_length=100,
        widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'О чем вы хотите написать?'})
    )
    email = forms.EmailField(
        label='Ваш Email',
        widget=forms.EmailInput(attrs={'class': 'form-control', 'placeholder': 'example@mail.com'})
    )
    text = forms.CharField(
        label='Сообщение',
        widget=forms.Textarea(attrs={'class': 'form-control', 'rows': 5, 'placeholder': 'Введите текст сообщения...'})
    )