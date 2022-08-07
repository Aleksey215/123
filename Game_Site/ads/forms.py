from django import forms
from .models import *
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class PostForm(forms.ModelForm):
    author = forms.CharField(widget=forms.TextInput(), required=True, max_length=32)
    title = forms.CharField(widget=forms.TextInput(), required=True, max_length=64)
    category = forms.CharField(widget=forms.TextInput(), required=True, max_length=32)
    content = RichTextUploadingField

    class Meta:
        model = Post
        fields = ('author', 'title', 'category', 'content')
