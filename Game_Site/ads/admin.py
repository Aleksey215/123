from django.contrib import admin
from django import forms

# для реализации расширенного поля содержания, с добавлением медиа файлов и т.п.
from ckeditor_uploader.widgets import CKEditorUploadingWidget

from .models import Post


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
