from django.urls import path
from . import views

urlpatterns = [
    path('genres/', views.genre_list),
    path('genres/<int:genre_pk>/', views.genre_detail),
    path('movies/', views.movie_list),
    path('movies/<int:movie_pk>/', views.movie_detail),
    path('movies/<int:movie_pk>/scores/', views.score_create),
]