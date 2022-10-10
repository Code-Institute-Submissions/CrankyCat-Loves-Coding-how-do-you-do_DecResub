from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    # path('', views.RecordEmo, name='recordemo'),
    path('<int:user_id>/', views.RecordEmo, name='recordemo'),
]
