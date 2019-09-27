from django.urls import path
from . import views

app_name = 'movies'

urlpatterns = [
    path('', views.movie_list, name="movie_list"),
    path('new/', views.new, name='new'),
    path('<int:movie_id>/', views.detail, name="detail"),
    path('<int:movie_id>/edit', views.edit, name="edit"),
    path('<int:movie_id>/scores/new/', views.score_new, name="score_new"),
    path('<int:movie_id>/scores/<int:score_id>/delete', views.score_delete, name='score_delete'),
]