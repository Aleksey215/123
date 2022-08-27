from django.contrib import admin
from ckeditor_uploader.widgets import CKEditorUploadingWidget
from django import forms

from .models import Category, Post, User


class PostAdminForm(forms.ModelForm):
    post_content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_name', 'pwd']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    list_display = ['id', 'post_author', 'post_title', 'post_category']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'category_name']
