from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<int:id>/', views.emo_box, name='emobox'),
    path(
        'show_emo/<pk>',
        views.show_emo,
        name='show_emo',
    ),
]
