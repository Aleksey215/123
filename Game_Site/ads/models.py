from django.db import models
from ckeditor.fields import RichTextField


class User(models.Model):
    user_name = models.CharField(max_length=64)
    pwd = models.CharField(max_length=64)

    def __str__(self):
        return self.user_name


class Category(models.Model):
    category_name = models.CharField(max_length=32, unique=True)

    def __str__(self):
        return self.category_name


class Post(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    title = models.CharField(max_length=64, unique=True)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    content = RichTextField(blank=True, null=True)

    def __str__(self):
        return f'{self.title}: {self.category}'
