from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.movie_list, name='movie_list'),
    path('<int:movie_id>/', views.movie_detail, name='movie_detail'),
    path('<int:movie_id>/delete', views.movie_delete, name='movie_delete'),


    path('<int:movie_id>/scores/create/', views.score_create, name='score_create'),
    path('<int:movie_id>/scores/<int:score_id>/delete', views.score_delete, name='score_delete'),
]