from django import forms
from .models import *


class PostForm(forms.ModelForm):
    """
    Создание формы для добавления публикации
    """

    class Meta:
        model = Post
        fields = ('author', 'title', 'category', 'content')

        widgets = {
            # поле "автор" заполнится автоматически
            'author': forms.HiddenInput(),
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'category': forms.Select(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
        }


class ResponseForm(forms.ModelForm):
    """
    Создание формы для отклика
    """

    class Meta:
        model = Response
        fields = ('author', 'text', 'post')
        labels = {
            "text": "Response content:"
        }

        widgets = {
            # поле "автор" заполнится автоматически
            'author': forms.HiddenInput(),
            'text': forms.TextInput(attrs={'class': 'form-control'}),
            # поле "объявление" заполнится автоматически
            'post': forms.HiddenInput(),
        }
