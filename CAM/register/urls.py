from django.urls import path
from . import views

urlpatterns = [
    path('register/', views.student_register, name='register'),
    path('login/', views.user_login, name='login'),
]