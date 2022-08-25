from django import forms
from .models import *


class PostForm(forms.ModelForm):

    class Meta:
        model = Post
        fields = ('post_author', 'post_title', 'post_category', 'post_content')

        widgets = {
            'post_author': forms.Select(attrs={'class': 'form-control'}),
            'post_title': forms.TextInput(attrs={'class': 'form-control'}),
            'post_category': forms.Select(attrs={'class': 'form-control'}),
            'post_content': forms.Textarea(attrs={'class': 'form-control'}),
        }
