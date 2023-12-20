from django.shortcuts import render, get_object_or_404
from .models import Post
from django.shortcuts import render, get_object_or_404, redirect
from .models import Post, Comment
from .forms import CommentForm
from django.core.paginator import Paginator, EmptyPage, PageNotAnInteger

def news_view(request):
    # Get all posts for the main content
    all_posts = Post.objects.all().order_by('-created_at')
    
    # Set the number of posts to display per page
    posts_per_page = 5

    # Use Paginator to paginate the queryset
    paginator = Paginator(all_posts, posts_per_page)

    # Get the current page number from the request's GET parameters
    page = request.GET.get('page')

    try:
        # Get the posts for the current page
        posts = paginator.page(page)
    except PageNotAnInteger:
        # If the page parameter is not an integer, set it to 1
        posts = paginator.page(1)
    except EmptyPage:
        # If the page parameter is out of range, deliver the last page
        posts = paginator.page(paginator.num_pages)

    # Get the most recent posts for the sidebar
    recent_posts = Post.objects.order_by('-created_at')[:5]

    gallerys = PhotoGallery.objects.all()

    # Pass the gallerys queryset to the template
    return render(request, 'news_app/news.html', {'posts': posts, 'recent_posts': recent_posts, 'gallerys': gallerys})


def post_detail_view(request, pk):
   
    post = get_object_or_404(Post, pk=pk)
    comments = post.comments.all()  # Retrieve all comments related to the post

    if request.method == 'POST':
        form = CommentForm(request.POST)
        if form.is_valid():
            comment = form.save(commit=False)
            comment.post = post
            comment.save()
            return redirect('post_detail', pk=pk)
    else:
        form = CommentForm()

    return render(request, 'news_app/post_detail.html', {'post': post, 'comments': comments, 'form': form})




from .models import PhotoGallery

def gallery_detail_view(request):
    gallerys = PhotoGallery.objects.all()
    return render(request, 'news_app/gallery_detail.html', {'gallerys': gallerys})



   


