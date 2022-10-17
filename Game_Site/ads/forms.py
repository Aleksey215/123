from django import forms
from .models import *


# создание формы для добавления публикации
class PostForm(forms.ModelForm):

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

    class Meta:
        model = Response
        fields = ('author', 'text', 'post')
        labels = {
            "text": "Response content:"
        }

        widgets = {
            'author': forms.HiddenInput(),
            'text': forms.TextInput(attrs={'class': 'form-control'}),
            'post': forms.HiddenInput(),
        }
