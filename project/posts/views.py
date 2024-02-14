from django.shortcuts import render, redirect
from .models import Posts
from .forms import PostsForm
from django.views.generic import DetailView, UpdateView, DeleteView


# Create your views here.

def model_page(request):
    if request.method == "POST":
        selected_items_ids = request.POST.getlist('selected_items')
        selected_posts = Posts.objects.filter(id__in=selected_items_ids)
        return render(request, 'posts/model_page.html', {'selected_posts': selected_posts})
    else:
        return redirect('posts_home')  # Или другая логика для GET-запроса

def posts_home(request):
    posts = Posts.objects.order_by('date')
    return render(request, 'posts/posts_home.html', {'posts' : posts})

class PostsDetailView(DetailView):
    model = Posts
    template_name = 'posts/detail_view.html'
    context_object_name = 'post'

class PostsUpdateView(UpdateView):
    model = Posts
    template_name = 'posts/create.html'
    success_url = '/posts/'
    form_class = PostsForm

class PostsDeleteView(DeleteView):
    model = Posts
    success_url = '/posts/'
    template_name = 'posts/posts_delete.html'

def create(request):
    error = ''
    if request.method == "POST":
        form = PostsForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('/posts/')
        else:
            error = 'Форма некорректно заполнена'


    form = PostsForm()
    data = {
        'form' : form,
        'error': error
    }
    return render(request, 'posts/create.html', data)





