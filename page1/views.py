from django.shortcuts import render
from django.http import HttpResponse
from .models import Post

# Create your views here.

def home_view(request):
    context = {
        'key': Post.objects.all()
    }
    return render(request, 'page1/home.html', context)

def view1(request):
    return render(request, 'page1/about.html', {'title': 'About'})
