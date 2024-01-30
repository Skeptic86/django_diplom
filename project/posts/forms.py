from .models import Posts
from django.forms import ModelForm, TextInput, DateInput, CheckboxInput, BooleanField, CheckboxSelectMultiple

class PostsForm(ModelForm):
    class Meta:
        model = Posts
        fields = ['theme', 'appointment', 'is_link', 'is_shkn', 'date']

        widgets = {
            "theme": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Тема поста'
            }),
            "appointment": TextInput(attrs={
                'class': 'form-control',
                'placeholder': 'Назначение поста (ресурс для которого предназначается пост)'
            }),
            "is_link": CheckboxInput(attrs={'class': 'checkbox-class'}),
            "is_shkn": CheckboxInput(attrs={'class': 'checkbox-class'}),
            "date": DateInput(attrs={
                'class': 'form-control',
                'placeholder': 'Дата поста'
            }),
            
        }