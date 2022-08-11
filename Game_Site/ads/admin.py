from django.contrib import admin

from .models import Category, Post, User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    list_display = ['id', 'user_name', 'pwd']


@admin.register(Post)
class PostAdmin(admin.ModelAdmin):
    list_display = ['id', 'post_author', 'post_title', 'post_category']


@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ['id', 'category_name']
