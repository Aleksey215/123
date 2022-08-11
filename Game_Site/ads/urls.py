from django.urls import path
from .views import *


urlpatterns = [
    path('', PostsView.as_view(), name='posts'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
]
