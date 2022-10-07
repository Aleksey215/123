from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django import forms
# подключение групп пользователей
from django.contrib.auth.models import Group

# подключение формы для регистрации
from allauth.account.forms import SignupForm


# форма создания нового пользователя
class BaseRegisterForm(UserCreationForm):
    email = forms.EmailField(label='Email')
    first_name = forms.CharField(label='Name')
    last_name = forms.CharField(label='Surname')

    # расширение стандартной формы и добавление своих полей
    class Meta:
        model = User
        fields = (
            'username',
            'first_name',
            'last_name',
            'email',
            'password1',
            'password2',
        )


# добавление пользователя в группу "basic" при регистрации
class BasicSignupForm(SignupForm):

    # переопределение метода, который выполнится при успешном заполнении формы регистрации
    def save(self, request):
        # получение зарегистрированного пользователя
        user = super(BasicSignupForm, self).save(request)
        # получение нужной группы
        basic_group = Group.objects.get(name='basic')
        # добавление пользователя в группу
        basic_group.user_set.add(user)
        return user
