from .models import Posts
from django.forms import ModelForm

class PostsForm(ModelForm):
    class Meta:
        model = Posts
        fields = ['theme', 'appointment', 'is_link', 'is_shkn', 'date']