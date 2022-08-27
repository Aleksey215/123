from django.db import models
from ckeditor.fields import RichTextField
from ckeditor_uploader.fields import RichTextUploadingField


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
    post_author = models.ForeignKey(User, on_delete=models.CASCADE)
    post_title = models.CharField(max_length=64, unique=True)
    post_category = models.ForeignKey(Category, on_delete=models.CASCADE)
    post_content = RichTextUploadingField(blank=True, null=True)

    def __str__(self):
        return f'{self.post_title}: {self.post_category}'

    def get_absolute_url(self):
        return f'/ads/{self.id}'


class Response(models.Model):
    response_author = models.ForeignKey(User, on_delete=models.CASCADE)

