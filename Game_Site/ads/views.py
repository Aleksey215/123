from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from .models import User, Post
from .forms import PostForm
from django.http import HttpResponse


class AddPostView(CreateView):
    model = Post
    template_name = 'ads/add_post.html'
    form_class = PostForm


class PostsView(ListView):
    model = Post
    template_name = 'ads/posts.html'
    context_object_name = 'posts'


class PostUpdateView(UpdateView):
    template_name = 'ads/add_post.html'
    form_class = PostForm

    def get_object(self, **kwargs):
        id = self.kwargs.get('pk')
        return Post.objects.get(pk=id)
