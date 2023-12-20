# news_app/urls.py
from django.urls import path
from .import views 

urlpatterns = [
    path('news/', views.news_view, name='news_view'),
    path('<int:pk>/', views.post_detail_view, name='post_detail'),
    path('gallery', views.gallery_detail_view, name='gallery_detail'),  
    
]


