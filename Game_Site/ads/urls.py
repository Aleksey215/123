from django.urls import path
from .views import home, AddPostView, SeePostView


urlpatterns = [
    path('', home, name='home'),
    path('add_post/', AddPostView.as_view(), name='add_post'),
    path('all_post/', SeePostView.as_view(), name='see_post'),
]
