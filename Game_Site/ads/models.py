from django.db import models
from django.contrib.auth.models import User

from ckeditor_uploader.fields import RichTextUploadingField


class Post(models.Model):
    TYPE = (
        ('tank', 'Танки'),
        ('heal', 'Хилы'),
        ('dd', 'ДД'),
        ('buyers', 'Торговцы'),
        ('gildmaster', 'Гилдмастеры'),
        ('quest', 'Квестгиверы'),
        ('smith', 'Кузнецы'),
        ('tanner', 'Кожевники'),
        ('potion', 'Зельевары'),
        ('spellmaster', 'Мастера заклинаний'),
    )
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None, blank=True)
    title = models.CharField(max_length=64, unique=True)
    category = models.CharField(max_length=16, choices=TYPE, default='tank')
    content = RichTextUploadingField(blank=True, null=True)

    def __str__(self):
        return f'{self.title}: {self.category}'

    def get_absolute_url(self):
        return f'/ads/{self.id}'


class Response(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    text = models.TextField()
    time_of_creation = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(Post, on_delete=models.CASCADE)
    status = models.BooleanField(default=False)

