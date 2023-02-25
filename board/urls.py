from django.contrib import admin
from django.urls import path

from .views import (BoardCreate, detail_func, good_func, list_func, login_func,
                    logout_func, read_func, signup_func)

urlpatterns = [
    path('signup/', signup_func, name='signup'),
    path('login/', login_func, name='login'),
    path('list/', list_func, name='list'),
    path('logout/', logout_func, name='logout'),
    path('list/<int:pk>', detail_func, name='detail'),
    path('good/<int:pk>', good_func, name='good'),
    path('read/<int:pk>', read_func, name='read'),
    path('create/', BoardCreate.as_view(), name='create'),
]
