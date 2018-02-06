from django.shortcuts import render, get_object_or_404, redirect
from .forms import SiteForm
from .models import Site

def home(request):
    return render(request, 'home/heroic.html',{})

def intranet(request):
    if request.method == 'POST':
        form = SiteForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.published_date = timezone.now()
            post.save()
            return redirect('')
    else:
        form = SiteForm()
    return render(request,'home/intranet.html',{'form':form})

# Create your views here.
