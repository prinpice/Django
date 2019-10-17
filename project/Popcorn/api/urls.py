from django.urls import path
from . import views
from rest_framework_swagger.views import get_swagger_view

app_name = 'api'

urlpatterns = [
    path('movies/', views.movie_list, name='movie_list'),
    path('movies/<int:movie_id>', views.movie_detail, name='movie_detail'),

    path('farmer/', views.farmer_list, name='farmer_board_list'),
    path('farmer/<int:farmer_id>', views.farmer_detail, name='farmer_detail'),

    # path('docs/', get_swagger_view(title='APIdoc'))

]