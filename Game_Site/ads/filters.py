import django_filters
# импорт всех моделей
from .models import Response, Post


# фильтр для модели затяжек (наследуемся от класса из приложения)
class ResponseFilter(django_filters.FilterSet):

    # создание поля для фильтрации по вину
    # выведутся все объекты, в которых есть символы, введенные в поле
    post_title = django_filters.ModelChoiceFilter(
        field_name='post',
        label='Заголовок объявления',
        lookup_expr='exact',
        queryset=Post.objects.filter(author=self.username)
    )
