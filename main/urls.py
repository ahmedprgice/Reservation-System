from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('facilities/', views.facilities, name='facilities'),
    path('reservations/', views.reservations, name='reservations'),
    path('profile/', views.update_profile, name='profile'),
    path('facilites/classes/', views.classes_view, name='classes'),
    path('facilites/labs/', views.labs_view, name='labs'),
    path('facilites/sportfacilites/', views.sportfacilites_view, name='sportfacilites'),
    path('facilites/privaterooms/', views.Private_Study_Rooms, name='privaterooms'),
]