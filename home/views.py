from django.shortcuts import render, get_object_or_404, redirect
from .forms import SiteForm
from .models import Site

def home(request):
    return render(request, 'home/intranet.html',{})



# Create your views here.
