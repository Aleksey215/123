from django.shortcuts import render, redirect
from django.http import HttpResponse
from django.core.cache import cache
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from django.contrib.auth.mixins import LoginRequiredMixin

from .models import Post, Response
from .forms import PostForm, ResponseForm
from .filters import ResponseFilter


# отображение домашней страницы
def home(request):
    return render(request, 'ads/home.html')


# добавление объявления
class AddPostView(LoginRequiredMixin, CreateView):
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
    ordering = ['-id']


# редактирование объявления
class PostUpdateView(UpdateView):
    model = Post
    template_name = 'ads/add_post.html'
    form_class = PostForm

    # получение данных по выбранному объявлению
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)


# получение подробной информации об объявлении
class PostDetailView(DetailView):
    model = Post
    template_name = 'ads/post_detail.html'
    form_class = PostForm
    # queryset = Post.objects.all()

    # переопределение метода получения объекта
    def get_object(self, *args, **kwargs):
        # забирает значение по ключу, если его нет, то забирает None.
        obj = cache.get(f'post-{self.kwargs["pk"]}', None)
        # если объекта нет в кэше, то получаем его и записываем в кэш
        if not obj:
            obj = super().get_object(*args, **kwargs)
            cache.set(f'post-{self.kwargs["pk"]}', obj)
        return obj

    # для доступа к редактированию только собственных постов
    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        obj = cache.get(f'post-{self.kwargs["pk"]}', None)
        author = obj.author
        user = self.request.user
        context['author_user'] = True if user == author else False
        context['response_form'] = ResponseForm()
        return context

    def post(self, request, pk):
        post = self.get_object(Post, pk=pk)
        form = ResponseForm(request.POST)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.post = post
            obj.author = self.request.user
            obj.save()
            return redirect('post_detail', post.pk)


class ResponsesView(ListView):
    model = Response
    template_name = 'ads/responses.html'
    context_object_name = 'responses'
    ordering = ['-time_of_creation']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        # my_filter = Post.objects.filter(author=user)
        # print(my_filter)
        context['user'] = user
        context['filter'] = ResponseFilter(self.request.GET, queryset=self.get_queryset())
        return context
