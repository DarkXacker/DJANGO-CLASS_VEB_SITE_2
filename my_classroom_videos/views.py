from .models import Video
from django.shortcuts import render

# Create your views here.

def index(request):
    videos = Video.objects.all()
    return render(request, 'my_classroom/my_classroom.html', context={'videos': videos})