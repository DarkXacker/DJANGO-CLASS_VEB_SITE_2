from unicodedata import name
from django.urls import path, include
from .views import PupilListView, PupilDetailView

urlpatterns = [
    path('', PupilListView.as_view(), name='pupil_list'),
    path('<int:pk>/', PupilDetailView.as_view(), name='pupil_detail'),
]