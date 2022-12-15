from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.add_emo, name='recordemo'),
    path(
        'update_emo/<pk>',
        views.update_emo,
        name='update_emo',
    ),
    path(
        'delete_emo/<pk>',
        views.delete_emo,
        name='delete_emo',
    ),
    
]
