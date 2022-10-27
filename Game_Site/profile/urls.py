from django.urls import path
from .views import IndexView, UsersPostsView, ResponsesForPostView, confirm_response

urlpatterns = [
    # сама страница профиля
    path('', IndexView.as_view(), name='profile'),
    # все объявления пользователя
    path('user_posts/', UsersPostsView.as_view(), name='users_posts'),
    # все отклики для выбранного объявления
    path('responses_for_post/<int:pk>', ResponsesForPostView.as_view(), name='response_for_post'),
    # принять(подтвердить) отклик на объявление
    path('responses_for_post/<int:pk>/confirm_response/', confirm_response, name='confirm_response'),
    ]
