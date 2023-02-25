from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.db import IntegrityError
from django.shortcuts import get_object_or_404, redirect, render
from django.urls import reverse_lazy
from django.views.generic import CreateView

from .models import BoardModel


def signup_func(request):
    if request.method == 'POST':
        username = request.POST['username']
        password = request.POST['password']
        try:
            user = User.objects.create_user(username, '', password)
            login(request, user)
            return redirect('list')
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
            return redirect('list')
        else:
            return render(request, 'login.html', {'context': 'not logged in'})
    return render(request, 'login.html',  {'context': 'get login page'})


# @login_required
def list_func(request):
    object_list = BoardModel.objects.all()
    return render(request, 'list.html', {'object_list': object_list})


def logout_func(request):
    logout(request)
    return redirect('login')


def detail_func(request, pk):
    object = get_object_or_404(BoardModel, pk=pk)
    return render(request, 'detail.html', {'object': object})


def good_func(request, pk):
    object = BoardModel.objects.get(pk=pk)
    object.good += 1
    object.save()
    return redirect('list')


def read_func(request, pk):
    object = BoardModel.objects.get(pk=pk)
    username = request.user.get_username()
    if object.read_text is None or username not in object.read_text:
        object.read += 1
        object.read_text = object.read_text + ' ' + \
            username if object.read_text is not None else username
        object.save()
    return redirect('list')


class BoardCreate(CreateView):
    template_name = 'create.html'
    model = BoardModel
    fields = ('title', 'content', 'sns_image', 'author')
    success_url = reverse_lazy('list')
