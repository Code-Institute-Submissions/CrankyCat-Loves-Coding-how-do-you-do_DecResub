from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<int:user_id>/', views.EmoBox, name='emobox'),
    path('edit_emobox/<int:user_id>/', views.EditEmoBox, name='edit_emobox'),
    path(
        'delete_emobox/<int:user_id>/',
        views.DeleteEmoBox,
        name='delete_emobox'
    ),
    path(
        'show_emo/<pk>',
        views.show_emo,
        name='show_emo',
    ),
]
