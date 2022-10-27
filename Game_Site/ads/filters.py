import django_filters

from .models import Response, Post


def get_post_queryset(request):
    """
    Для фильтрации по объявлениям, которые созданы текущим пользователем.
    :param request:
    :return:
    """
    queryset = Post.objects.filter(author=request.user)
    return queryset


class ResponseFilter(django_filters.FilterSet):
    """
    Фильтр для страницы с откликами на объявления текущего пользователя
    """
    post_title = django_filters.ModelChoiceFilter(
        field_name='post',
        label='Choose ad for title',
        lookup_expr='exact',
        queryset=get_post_queryset
    )
