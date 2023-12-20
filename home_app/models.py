# models.py
from django.db import models

class HomeModel(models.Model):
    theme_of_semester = models.TextField(max_length=1000)
    picture_of_semester = models.ImageField(upload_to='images/', blank=True, null=True)
    content = models.TextField(max_length=500)
    theme_of_week = models.TextField(max_length=1000)
    picture_of_week = models.ImageField(upload_to='images/', blank=True, null=True)
    malengo_title = models.CharField(max_length=255)
    categories = models.TextField(max_length=400, default='')
    malengo_content = models.TextField(max_length=10000)
    malengo_created_at = models.DateTimeField(auto_now_add=True)







class Leader(models.Model):
    name = models.CharField(max_length=100)
    role = models.CharField(max_length=100)
    image = models.ImageField(upload_to='leaders/')
    additional_image = models.ImageField(upload_to='leaders/additional_images/', blank=True, null=True)
    course = models.CharField(max_length=100)
    year = models.IntegerField()
    created_at = models.DateTimeField(auto_now_add=True)  # Add the created_at field

    

    def __str__(self):
        return self.name



# models.py

from django.db import models

class AboutUsContent(models.Model):
    DIVISION_CHOICES = [
        ('History', 'History'),
        ('MissionVision', 'Mission & Vision'),
    ]

    title = models.CharField(max_length=255)
    division = models.CharField(max_length=20, choices=DIVISION_CHOICES, default='History')
    meta = models.CharField(max_length=255)
    image = models.ImageField(upload_to='about_us_images/', blank=True, null=True)
    content = models.TextField(max_length=10000)

    def __str__(self):
        return f"{self.title} - {self.division}"
