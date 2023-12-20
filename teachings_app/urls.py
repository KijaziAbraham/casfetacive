from django.urls import path
from .views import  articles_view, audios_view, videos_view, books_view

urlpatterns = [
    path('articles/', articles_view, name='articles_view'),
    path('audios/', audios_view, name='audios_view'),
    path('videos/', videos_view, name='videos_view'),
    path('books/', books_view, name='books_view'),
]
