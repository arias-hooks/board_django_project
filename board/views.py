from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import render

# Create your views here.


def signup_func(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            User.objects.create_user(username, '', password)
            return render(request, 'signup.html', {'some': 100})
        except IntegrityError:
            return render(request, 'signup.html', {'error': 'このユーザーは既に登録されています'})

    return render(request, 'signup.html', {'some': 100})


def login_func(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return render(request, 'login.html', {'context': 'logged in'})
        else:
            return render(request, 'login.html', {'context': 'not logged in'})
    return render(request, 'login.html',  {'context': 'get login page'})
