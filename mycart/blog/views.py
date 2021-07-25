from django.shortcuts import render
from django.http import HttpResponse
from .models import Blogpost
# Create your views here.

def blogPost(request, id):
    return render(request, 'blog/blogPost.html')

def index(request):
    blog = Blogpost.object
    return render(request, 'blog/index.html')