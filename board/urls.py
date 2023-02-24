from django.contrib import admin
from django.urls import path

from .views import login_func, signup_func

urlpatterns = [
    path('signup/', signup_func, name='signup'),
    path('login/', login_func, name='login'),
]
