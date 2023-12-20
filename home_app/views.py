from news_app.models import Post
from django.shortcuts import render
from django.core.mail import send_mail
from django.http import JsonResponse
from. forms import ContactForm
from .models import HomeModel,Leader
from django.shortcuts import render, get_object_or_404
from django.core.mail import send_mail
from django.http import JsonResponse
from datetime import timedelta
from django.utils import timezone
from .models import AboutUsContent


def home_view(request):
    home_data = HomeModel.objects.first()
    recent_posts = Post.objects.order_by('-created_at')[:5]

    context = {
        'home_data': home_data,
        'recent_posts': recent_posts,
    }

    return render(request, 'home_app/home.html', context)


def contact_view(request):

    return render(request, 'home_app/contact.html')
    

def about_view(request):
    history_contents = AboutUsContent.objects.filter(division='History')
    mission_vision_contents = AboutUsContent.objects.filter(division='MissionVision')

    leaders = Leader.objects.all()
    academic_year_start = leaders[0].created_at
    next_academic_year = academic_year_start + timedelta(days=365)  

    latest_post = Post.objects.latest('created_at')

    context = {
        'leaders': leaders,
        'next_academic_year': next_academic_year.year,
        'history_contents': history_contents,
        'mission_vision_contents': mission_vision_contents,
        'latest_post': latest_post,

    }
    
    return render(request, 'home_app/about.html', context)



def home_detail_view(request, pk):
    home_data = get_object_or_404(HomeModel, pk=pk)
    context = {'home_data': home_data}
    return render(request, 'home_app/home_detail.html', context)




def send_feedback(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        subject = request.POST.get('subject', '')
        message = request.POST.get('message', '')

      
        admin_email = 'abrahamkijazi02@example.com'

        send_mail(
            f'Feedback: {subject}',
            f'Name: {name}\nEmail: {email}\nMessage: {message}',
            email,
            [admin_email],
            fail_silently=False,
        )

        return JsonResponse({'message': 'success'})
    else:
        return JsonResponse({'message': 'error'})











    


