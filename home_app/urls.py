from django.urls import path
from. import views

urlpatterns=[
    path('',views.home_view, name='home_view'),
    path('contact/',views.contact_view, name='contact_view'),
    path('about/',views.about_view, name='about_view'),
    path('<int:pk>/', views.home_detail_view, name='home_detail_view'),
    path('send_feedback/', views.send_feedback, name='send_feedback'),

    
]