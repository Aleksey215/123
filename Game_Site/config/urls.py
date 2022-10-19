from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    # админка
    path('admin/', admin.site.urls),
    # приложение для объявлений
    path('', include('ads.urls')),
    # для регистрации, входа и выхода
    path('accounts/', include('allauth.urls')),
    # профиль пользователя для хранения приватной информации
    path('profile/', include('profile.urls')),
    # подключение расширенного редактора текста с добавлением медиа файлов
    path('ckeditor', include('ckeditor_uploader.urls')),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)  # задаем путь
