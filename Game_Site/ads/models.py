from django.db import models
from django.contrib.auth.models import User

# для использования расширенного поля
from ckeditor_uploader.fields import RichTextUploadingField


# модель самого объявления, которое создает пользователь
class Post(models.Model):
    # категории публикаций
    TYPE = (
        ('tank', 'Tanks'),
        ('heal', 'Heals'),
        ('dd', 'DD'),
        ('buyers', 'Merchants'),
        ('gildmaster', 'Gildmasters'),
        ('quest', 'Quest'),
        ('smith', 'Blacksmiths'),
        ('tanner', 'Tanners'),
        ('potion', 'Potions'),
        ('spellmaster', 'Spell masters'),
    )
    # данное поле заполнится автоматически, именем зарегистрированного пользователя, который создает пост
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None, blank=True)
    title = models.CharField(max_length=64, unique=True)
    category = models.CharField(max_length=16, choices=TYPE, default='tank')
    # подключение расширенного поля для содержания поста
    content = RichTextUploadingField(blank=True, null=True)

    def __str__(self):
        return f'Title:{self.title}'

    def get_absolute_url(self):
        return f'/posts/'


# модель отклика на объявление
class Response(models.Model):
    author = models.ForeignKey(User, on_delete=models.CASCADE, default=None, blank=True)
    text = models.TextField()
    time_of_creation = models.DateTimeField(auto_now_add=True)
    post = models.ForeignKey(
        Post,
        on_delete=models.CASCADE,
        default=None,
        blank=True,
        related_name='response'
    )
    confirmed = models.BooleanField(default=False)

    def __str__(self):
        return f'Response to:{self.post.title}'

    def get_absolute_url(self):
        return f'/posts/'
