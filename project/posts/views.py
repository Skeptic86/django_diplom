from django.shortcuts import render
from .models import Posts

# Create your views here.
def posts_home(request):
    posts = Posts.objects.order_by('date')
    return render(request, 'posts/posts_home.html', {'posts' : posts})

def create(request):
    posts = Posts.objects.order_by('date')
    return render(request, 'posts/create.html', {'posts' : posts})