from django import forms
from .models import *
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


class PostForm(forms.ModelForm):
    post_author = forms.CharField(widget=forms.TextInput(), required=True, max_length=32)
    post_title = forms.CharField(widget=forms.TextInput(), required=True, max_length=64)
    post_category = forms.CharField(widget=forms.TextInput(), required=True, max_length=32)
    post_content = RichTextUploadingField

    class Meta:
        model = Post
        fields = ('post_author', 'post_title', 'post_category', 'post_content')
