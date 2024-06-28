from django.urls import path
from . import views

app_name = 'core'

urlpatterns = [
    path('', views.home, name='home'),
    path('profile-list/', views.profile, name='profile'),
    path('create-profile/', views.create_profile, name='create_profile'),
    path('watch/<uuid:pk>/', views.profile_detail, name='profile_detail'),
    path('movie/detail/<uuid:pk>/', views.movie_detail, name='movie_detail'),
    path('movie/play/<uuid:pk>/', views.show_movie, name='show_movie')
]
