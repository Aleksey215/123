from django.shortcuts import render
from django.views.generic import ListView, CreateView, UpdateView, DetailView
from .models import User, Post
from .forms import PostForm
from django.http import HttpResponse


class AddPostView(CreateView):
    model = Post
    template_name = 'ads/add_post.html'
    form_class = PostForm


# class AddPostView(ListView):
#     model = Post
#
#     def get(self, request):
#         form = PostForm()
#         return render(request, 'app1/index.html', {'form':form})
#     def post(self, request):
#         form = PostForm(request.POST)
#         if form.is_valid():
#             userName = form.cleaned_data['userName']
#             title = form.cleaned_data['title']
#             content = form.cleaned_data['content']
#
#             user_obj = User.objects.get(user_name=userName)
#             add_post = Post.objects.create(user=user_obj, title=title, content=content)
#             add_post.save()
#             form = PostForm()
#             return render(request,'app1/index.html',{'form':form})


class PostsView(ListView):
    model = Post
    template_name = 'ads/posts.html'
    context_object_name = 'post'

