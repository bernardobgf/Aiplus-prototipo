from django.contrib import admin
from django.urls import path
from core import views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.home, name='home'),
    path('dashboard/', views.dashboard, name='dashboard'),
    path('settings/', views.settings_view, name='settings'),
    path('api/chat/', views.chat_api, name='chat_api'),
    path('clear/', views.clear_chat, name='clear_chat'),
]