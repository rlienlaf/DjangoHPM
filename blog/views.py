from django.http import Http404
from django.shortcuts import render, get_object_or_404
from django.utils import timezone
from .models import Post

def index(request):
    latest_posts = Post.objects.order_by('-published_date')[:10]
    context= {'latest_posts': latest_posts}
    return render(request, 'blog/index.html' , context)

def detail(request, pk):
    post= get_object_or_404(Post,pk=pk)
    return render(request, 'blog/detail.html', {'post':post})

def post_list(request):
    #posts = Post.objects.filter(published_date__lte=timezone.now()).order_by('-published_date')
    posts = Post.objects.order_by('-published_date')[:10]
    context= {'posts': posts}
    return render(request, 'blog/post_list.html', context)


# Create your views here.
