from django.shortcuts import render, redirect
from django.views.generic import ListView, CreateView, UpdateView, DetailView, DeleteView
from django.contrib.auth.mixins import LoginRequiredMixin
from django_filters.views import FilterView
# для перевода html в текст для отправки в таску
from django.template.loader import render_to_string

from .models import Post, Response, User
from .forms import PostForm, ResponseForm
from .filters import ResponseFilter
from .tasks import email_for_post_author_task, email_for_response_author_task


def send_mail_to_post_author(instance):
    post_author = instance.post.author.username
    post_title = instance.post.title
    post_author_email = instance.post.author.email
    response_author = instance.author.username
    response_content = instance.text
    html_content = render_to_string(
        'ads/post_mail.html',
        {'post_title': post_title,
         'response_author': response_author,
         'response_content': response_content}
    )
    email_for_post_author_task.delay(post_author, post_author_email, html_content)


def send_mail_to_response_author(instance):
    post_author = instance.post.author.username
    post_title = instance.post.title
    response_author = instance.author.username
    response_content = instance.text
    response_author_email = instance.author.email
    html_content = render_to_string(
        'ads/response_mail.html',
        {'post_title': post_title,
         'post_author': post_author,
         'response_content': response_content}
    )
    email_for_response_author_task.delay(response_author, response_author_email, html_content)


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
    paginate_by = 5


# редактирование объявления
class PostUpdateView(UpdateView):
    model = Post
    template_name = 'ads/add_post.html'
    form_class = PostForm

    # получение данных по выбранному объявлению
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        post = Post.objects.get(pk=id)
        return post


# получение подробной информации об объявлении
class PostDetailView(DetailView):
    model = Post
    template_name = 'ads/post_detail.html'
    form_class = PostForm

    # получение данных по выбранному объявлению
    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        obj = Post.objects.get(pk=id)
        return obj

    def get_context_data(self, **kwargs):
        # в своих объявлениях пользователь может редактировать их
        # в чужих может оставить отклик
        context = super().get_context_data(**kwargs)
        id = self.kwargs.get('pk')
        obj = Post.objects.get(pk=id)
        author = obj.author
        user = self.request.user
        # для отображения формы только зарегистрированным пользователям
        context['anonymous'] = user in User.objects.all()
        # для доступа к редактированию только собственных постов
        context['author_user'] = True if user == author else False
        # для добавления формы отклика на страницу
        context['response_form'] = ResponseForm()
        return context

    # для добавления формы отклика на страницу объявления
    # пользователь может оставить отклик на странице post_detail
    def post(self, request, pk):
        post = self.get_object(pk=pk)
        form = ResponseForm(request.POST)

        if form.is_valid():
            obj = form.save(commit=False)
            obj.post = post
            obj.author = self.request.user
            obj.save()
            return redirect('post_detail', post.pk)


class PostDeleteView(DeleteView):
    template_name = 'ads/post_delete.html'
    queryset = Post.objects.all()
    success_url = '/posts/'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        id = self.kwargs.get('pk')
        obj = Post.objects.get(pk=id)
        responses = Response.objects.filter(post__id=obj.id)
        context['responses'] = responses
        return context


# Отображение всех откликов
class ResponsesView(FilterView):
    model = Response
    filterset_class = ResponseFilter
    template_name = 'ads/responses.html'
    context_object_name = 'responses'
    ordering = ['-time_of_creation']

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        user = self.request.user
        # для отображения в шаблоне только тех откликов, которые оставлены
        # к объявлениям текущего пользователя
        context['user'] = user
        return context


class ResponseDeleteView(DeleteView):
    template_name = 'ads/response_delete.html'
    queryset = Response.objects.all()
    success_url = '/responses/'


def accept_response(request, **kwargs):
    pk = request.GET.get('pk', )
    response = Response.objects.get(pk=pk)
    response.confirmed = True
    response.save()
    return redirect('/responses/')
