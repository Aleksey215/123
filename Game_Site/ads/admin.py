from django.contrib import admin
from django import forms

# для реализации расширенного поля содержания, с добавлением медиа файлов и т.п.
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import Post, Response


# добавление в админку расширенного поля
class PostAdminForm(forms.ModelForm):
    # подключение виджета для поля
    content = forms.CharField(widget=CKEditorUploadingWidget())

    class Meta:
        model = Post
        fields = '__all__'


# регистрация модели для админки
@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    form = PostAdminForm
    list_display = ['id', 'author', 'title', 'category']


class ResponseAdminForm(forms.ModelForm):

    class Meta:
        model = Response
        fields = '__all__'


@admin.register(Response)
class ResponseAdmin(admin.ModelAdmin):
    form = ResponseAdminForm
    list_display = ['id', 'author', 'text', 'time_of_creation', 'post', 'status']
