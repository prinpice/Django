from django.urls import path
from . import views

app_name = 'accounts'
urlpatterns = [
    path('signup/', views.signup, name='signup'),
    path('login/', views.login, name='login'),
    path('logout/', views.logout, name='logout'),
    path('', views.user_list, name="user_list"),
    path('<int:user_id>', views.people, name="people"),
    path('<int:user_id>/follow/', views.follow, name="follow"),
    path('<int:user_id>/followings/', views.followings, name="followings"),
    path('<int:user_id>/followers/', views.followers, name="followers"),
]