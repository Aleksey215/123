from django.urls import path
from .views import *

urlpatterns = [
    path('', home, name='home'),
    path('posts/', PostsView.as_view(), name='posts'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('ads/<int:pk>/', PostDetailView.as_view(), name='post_detail'),
    path('add_post/<int:pk>', PostUpdateView.as_view(), name='post_update'),
    path('responses/', ResponsesView.as_view(), name='responses'),
    path('responses/accept_response/', accept_response, name='accept_response'),
    path('response_delete<int:pk>/', ResponseDeleteView.as_view(), name='response_delete'),
]
