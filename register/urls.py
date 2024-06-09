from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.register, name='register'),
    path('login/', views.user_login, name='login'),
    path('register_staff/', views.register_staff, name='register_staff'),
    path('register_student/', views.register_student, name='register_student'),
]