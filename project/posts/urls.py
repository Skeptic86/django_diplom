from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.posts_home, name='posts_home')
]
