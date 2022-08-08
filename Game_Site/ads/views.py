from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from .models import User, Post
from .forms import PostForm
from django.http import HttpResponse


class AddPostView(CreateView):
    template_name = 'ads/add_post.html'
    form = PostForm()


class PostsView(ListView):
    model = Post
    template_name = 'ads/posts.html'
    context_object_name = 'post'


    # def post(self, request):
    #     if form.is_valid():
    #         author = form.cleaned_data['author']
    #         title = form.cleaned_data['title']
    #         category = form.cleaned_data['category']
    #         content = form.cleaned_data['content']
    #
    #         user_obj = User.objects.get(user_name=author)
    #         add_post = Post.objects.create(user=user_obj, title=title, category=category, content=content)
    #         add_post.save()
    #         form = PostForm()
    #         return render(request, 'ads/index.html', {'form': form})

