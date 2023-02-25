from django.contrib import admin
from django.urls import path

from .views import list_func, login_func, logout_func, signup_func

urlpatterns = [
    path('signup/', signup_func, name='signup'),
    path('login/', login_func, name='login'),
    path('list/', list_func, name='list'),
    path('logout/', logout_func, name='logout'),
]
