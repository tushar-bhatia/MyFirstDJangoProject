from MyFirstDJangoProject.settings import BASE_DIR
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import messages
from django.contrib import auth
import os

# Create your views here.

def register(request):
    if request.method == 'POST':
        first_name = request.POST['first_name']
        last_name = request.POST['last_name']
        email = request.POST['email']
        username = request.POST['username']
        password1 = request.POST['password1']
        password2 = request.POST['password2']
        if password1 == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request, 'Email already exists!')
                return redirect('register')
            elif User.objects.filter(username=username).exists():
                messages.info(request, 'Username Already exists!')
                return redirect('register')
            else:
                user = User.objects.create_user(first_name=first_name, last_name=last_name, email=email, username=username, password=password1)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Passwords do not match!')
            return redirect('register')
    else:
        return render(request, os.path.join(BASE_DIR, 'accounts/templates/register.html'))



def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']
        username = User.objects.get(email=email).username
        user = auth.authenticate(username=username, password=password)
        if user is not None:
            auth.login(request, user)
            return redirect("/")
        else:
            messages.error(request, 'Invalid Credentials!')
            return redirect('login')
    else:
        return render(request, os.path.join(BASE_DIR, 'accounts/templates/login.html'))

def logout(request):
    auth.logout(request)
    return redirect('/')
