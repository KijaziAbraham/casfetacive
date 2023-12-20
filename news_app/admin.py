from django.contrib import admin
from .models import Category, Post, Author, PhotoGallery, InstagramPost

admin.site.register(Category)
admin.site.register(Post)
admin.site.register(Author)
admin.site.register(PhotoGallery)
admin.site.register(InstagramPost)


