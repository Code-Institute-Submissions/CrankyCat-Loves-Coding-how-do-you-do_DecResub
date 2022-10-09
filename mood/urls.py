from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.Mood, name='mood'),
    path('how_it_works/', views.HowItWork, name='howitworks'),
]
