from django.views.generic import DetailView
from django.shortcuts import render
from .models import Video

# Create your views here. 

def index(request): 
    video=Video.objects.all() 
    return render(request,"news_site/news_site.html",{"video":video})