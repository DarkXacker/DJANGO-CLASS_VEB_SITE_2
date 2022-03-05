from operator import mod
from re import template
from django.views.generic import ListView, DetailView
from .models import Pupil

# Create your views here.

class PupilListView(ListView):
    model = Pupil
    template_name = 'pupils/pupil_list.html'

class PupilDetailView(DetailView):
    model = Pupil
    template_name = 'pupils/pupil_detail.html'
