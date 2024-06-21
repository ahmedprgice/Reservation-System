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

    # path('facilites/classes/', views.classes_view, name='classes'),
    # path('facilites/labs/', views.labs_view, name='labs'),
    # path('facilites/sportfacilites/', views.sportfacilites_view, name='sportfacilites'),
    # path('facilites/privaterooms/', views.Private_Study_Rooms, name='privaterooms'),
    path('reservations/', views.reservations, name='reservations'),
    # Add the cancel_reservation URL
    path('cancel_reservation/<int:reservation_id>/', views.cancel_reservation, name='cancel_reservation'),
    
]