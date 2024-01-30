from django.shortcuts import render, redirect
from .models import Posts
from .forms import PostsForm
from django.views.generic import DetailView


# Create your views here.
def posts_home(request):
    posts = Posts.objects.order_by('date')
    return render(request, 'posts/posts_home.html', {'posts' : posts})

class PostsDetailView(DetailView):
    model = Posts
    template_name = 'posts/detail_view.html'
    context_object_name = 'post'

def create(request):
    error = ''
    if request.method == "POST":
        form = PostsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('home')
        else:
            error = 'Форма некорректно заполнена'


    form = PostsForm()
    data = {
        'form' : form,
        'error': error
    }
    return render(request, 'posts/create.html', data)