from django.urls import path

from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('home/', views.home, name='home'),
    path('facilities/', views.facilities, name='facilities'),
    path('facilities/<str:facility_anemity>/', views.facility_anemity, name='facility_anemity'),
    path('reservations/', views.reservations, name='reservations'),
    path('profile/', views.update_profile, name='profile'),
    path('changepassword/', views.change_password, name='changepassword'),
    path('reservations/', views.reservations, name='reservations'),
    path('reviews/', views.reviews, name='reviews'),
    path('cancel_reservation/<int:reservation_id>/', views.cancel_reservation, name='cancel_reservation'),
     path('add_review/<int:facility_id>/', views.add_review, name='add_review'),
]