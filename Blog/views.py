from django.shortcuts import render
from .models import Post
from django.utils import timezone

def home(request):
    posts = Post.objects.all().order_by('published_date')
    return render(request, 'Blog/home.html', {'posts':posts})
