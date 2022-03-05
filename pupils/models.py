from distutils.command.upload import upload
from operator import mod
from turtle import st
from django.contrib.auth import get_user_model
from django.db import models
from django.urls import reverse

# Create your models here.

class Pupil(models.Model):
    title = models.CharField(max_length=150)
    body = models.TextField()
    photo = models.ImageField(upload_to = 'images/', blank = True)

    def __str__(self):
        return self.title

    def get_absolute_url(self):
        return reverse('pupils_detail', args=[str(self.id)])