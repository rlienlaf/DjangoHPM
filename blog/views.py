from django.http import Http404
from django.shortcuts import render, get_object_or_404, redirect
from django.utils import timezone
from .forms import PostForm
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

def new_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog:detail', pk=post.pk)
    else:
        form = PostForm()
    return render(request, 'blog/edit_post.html', {'form': form})

def edit_post(request, pk):
    post = get_object_or_404(Post, pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST, instance=post)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('blog:detail', pk=post.pk)
    else:
        form = PostForm(instance=post)
    return render(request, 'blog/edit_post.html', {'form': form})

# Create your views here.
