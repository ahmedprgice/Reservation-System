from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('home/', views.home, name='home'),
    path('facilities/', views.facilities, name='facilities'),
    path('reservations/', views.reservations, name='reservations'),
    path('profile/', views.profile, name='profile'),
    
]