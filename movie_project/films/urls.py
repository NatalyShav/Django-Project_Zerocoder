from django.urls import path
from . import views

urlpatterns = [
    path('add/', views.add_film, name='add_film'),
    path('', views.list_films, name='list_films'),
]