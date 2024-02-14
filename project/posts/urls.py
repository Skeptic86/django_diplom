from django.urls import path, include
from . import views

urlpatterns = [
    path('', views.posts_home, name='posts_home'),
    path('model_page', views.model_page, name='model_page'),
    path('create', views.create, name='create'),
    path('<int:pk>', views.PostsDetailView.as_view(), name='posts_detail'),
    path('update/<int:pk>', views.PostsUpdateView.as_view(), name='posts_update'),
    path('delete/<int:pk>', views.PostsDeleteView.as_view(), name='posts_delete'),
]
