from django.shortcuts import render, redirect, reverse
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm

from .forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form =  SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            raw_password = form.cleaned_data.get('password1')
            user = authenticate(username=username, password=raw_password)
            login(request, user)
    else:
        form = SignUpForm()
    return render(request, 'core/signup.html', {'form': form})



# Create your views here.
