from django.shortcuts import render
from .models import Article, Video, Book, Audio
from .forms import ArticleForm, VideoForm, BookForm, AudioForm

def articles_view(request):
    articles = Article.objects.all()
    return render(request, 'teachings_app/articles.html', {'articles': articles})

def audios_view(request):
    audios = Audio.objects.all()
    return render(request, 'teachings_app/audios.html', {'audios': audios})

def videos_view(request):
    videos = Video.objects.all().order_by('-video_created_at')
    return render(request, 'teachings_app/videos.html', {'videos': videos})


def books_view(request):
    books = Book.objects.all()
    return render(request, 'teachings_app/books.html', {'books': books})


# Create your views here.
