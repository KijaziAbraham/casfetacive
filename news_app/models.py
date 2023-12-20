from django.db import models
from django.contrib.auth.models import User

class Category(models.Model):
    name = models.CharField(max_length=255)

class Author(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    bio = models.TextField()

class Post(models.Model):
    title = models.CharField(max_length=255)
    content = models.TextField()
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    image = models.ImageField(upload_to='images/', null=True, blank=True)
    audio = models.FileField(upload_to='audios/', null=True, blank=True)
    video = models.FileField(upload_to='videos/', null=True, blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    author = models.ForeignKey(Author, on_delete=models.CASCADE, related_name='posts')

    def __str__(self):
        return self.title




# models.py

from django.db import models

class PhotoGallery(models.Model):
    title = models.CharField(max_length=255)
    created_at = models.DateTimeField(auto_now_add=True)
    image = models.ImageField(upload_to='photo_gallery/')

    def __str__(self):
        return self.title


class InstagramPost(models.Model):
    image = models.ImageField(upload_to='instagram_posts/')
    caption = models.TextField()






# models.py
from django.db import models

class Comment(models.Model):
    post = models.ForeignKey('news_app.Post', on_delete=models.CASCADE, related_name='comments')
    name = models.CharField(max_length=100)
    email = models.EmailField(null=False, blank=False)
    subject = models.CharField(max_length=100)
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'{self.name} - {self.subject}'



    
