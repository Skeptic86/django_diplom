from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.posts_home, name='posts_home'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.PostsDetailView.as_view(), name='posts_detail')
]
