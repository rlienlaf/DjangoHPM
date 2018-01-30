from django.http import Http404
from django.shortcuts import render
from .models import Post

def index(request):
    latest_posts = Post.objects.order_by('-published_date')[:10]
    context= {'latest_posts': latest_posts}
    return render(request, 'blog/index.html' , context)

def detail(request, post_id):
    post= get_object_or_404(Post,pk=post_id)
    return render(request, 'blog/detail.html', {'post':post})

# Create your views here.
