from django.db import models

class Article(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    article_created_at=models.DateTimeField( auto_now_add=True )


class Video(models.Model):
    title = models.CharField(max_length=255)
    video_file = models.FileField(upload_to='videos/', null=True, blank=True)
    thumbnail_image = models.ImageField(upload_to='thumbnails/', blank=True, null=True)
    video_created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title



class Book(models.Model):
    title = models.CharField(max_length=255)
    author = models.CharField(max_length=255)
    content = models.FileField(upload_to='books/pdfs/')   
    book_created_at = models.DateTimeField(auto_now_add=True)


class Audio(models.Model):
    title = models.CharField(max_length=255)
    audio_file = models.FileField(upload_to='audios/', null=True, blank=True)
    audio_created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.title

