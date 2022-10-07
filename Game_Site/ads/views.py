from django.shortcuts import render
from django.http import HttpResponse
from django.core.cache import cache
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import User, Post
from .forms import PostForm


# отображение домашней страницы
def home(request):
    return render(request, 'ads/home.html')


# добавление объявления
class AddPostView(CreateView):
    template_name = 'ads/add_post.html'
    form_class = PostForm

    # автоматическое заполнение поля "автор"
    def form_valid(self, form):
        form.instance.author = self.request.user
        return super(AddPostView, self).form_valid(form)


# отображение всех объявлений
class PostsView(ListView):
    model = Post
    template_name = 'ads/posts.html'
    context_object_name = 'posts'


# редактирование объявления
class PostUpdateView(UpdateView):
    template_name = 'ads/add_post.html'
    form_class = PostForm

    # получение данных по выбранному объявлению
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


# получение подробной информации об объявлении
class PostDetailView(DetailView):
    template_name = 'ads/post_detail.html'
    form_class = PostForm
    queryset = Post.objects.all()

    # переопределение метода получения объекта
    def get_object(self, *args, **kwargs):
        # забирает значение по ключу, если его нет, то забирает None.
        obj = cache.get(f'post-{self.kwargs["pk"]}', None)
        # если объекта нет в кэше, то получаем его и записываем в кэш
        if not obj:
            obj = super().get_object(*args, **kwargs)
            cache.set(f'post-{self.kwargs["pk"]}', obj)
        return obj
