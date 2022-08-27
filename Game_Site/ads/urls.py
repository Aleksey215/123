from django.urls import path
from .views import *

urlpatterns = [
    path('', PostsView.as_view(), name='posts'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('add_post/<int:pk>', PostUpdateView.as_view(), name='post_update'),
]
