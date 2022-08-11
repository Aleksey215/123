from django import forms
from .models import *
from ckeditor.widgets import CKEditorWidget


class PostForm(forms.ModelForm):
    post_content = forms.CharField(widget=CKEditorWidget())

    class Meta:
        model = Post
        fields = ('post_author', 'post_title', 'post_category', 'post_content')
