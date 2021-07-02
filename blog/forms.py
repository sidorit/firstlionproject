from django import forms
from .models import Blog

class BlogForm(forms.ModelForm):
    class Meta: #밑의 정보로 BlogForm을 만들겠다 이런느낌
        model=Blog
        fields=['title', 'writer', 'body', 'image']

