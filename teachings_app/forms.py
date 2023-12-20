from django import forms
from .models import Article, Video, Book, Audio

class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ['title', 'content']

class VideoForm(forms.ModelForm):
    class Meta:
        model = Video
        fields = ['title', 'video_file']

class BookForm(forms.ModelForm):
    class Meta:
        model = Book
        fields = ['title', 'author', 'content']

class AudioForm(forms.ModelForm):
    class Meta:
        model = Audio
        fields = ['title', 'audio_file']
