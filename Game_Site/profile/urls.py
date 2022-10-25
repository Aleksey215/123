from django.urls import path
from .views import IndexView, UsersPostsView, ResponsesForPostView, confirm_response

# перенаправляемся на единственное представление IndexView, которое описано в соответствующем файле views.py
urlpatterns = [
    path('', IndexView.as_view(), name='profile'),
    path('user_posts/', UsersPostsView.as_view(), name='users_posts'),
    path('responses_for_post/<int:pk>', ResponsesForPostView.as_view(), name='response_for_post'),
    path('responses_for_post/<int:pk>/confirm_response/', confirm_response, name='confirm_response'),
    ]
