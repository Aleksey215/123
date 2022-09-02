from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView

from .views import BaseRegisterView


urlpatterns = [
    path('login/',
         LoginView.as_view(template_name='sign/login.html'),  # указываем шаблон для вывода формы
         name='login'),  # устанавливаем имена для этих URL в целях удобства обращения к ним из шаблонов
    path('logout/',
         LogoutView.as_view(template_name='sign/logout.html'),  # указываем шаблон для вывода формы
         # При выходе с сайта (вспоминаем кнопку, которую мы создали раньше в шаблоне profile.html)
         # Django перенаправит пользователя на страницу, указанную в параметре template_name класса LogoutView.
         name='logout'),  # устанавливаем имена для этих URL в целях удобства обращения к ним из шаблонов
    path('signup/',
         BaseRegisterView.as_view(template_name='sign/signup.html'),
         name='signup'),
]
