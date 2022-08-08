from django.urls import path
from .views import *


urlpatterns = [
    path('', PostsView.as_view(), name='posts'),
]
