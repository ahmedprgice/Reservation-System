from django.shortcuts import render
from .models import Student, Staff, Reservation, Reviews, Facility, Facaulty
# Create your views here.

def index(response):
    return render(response, "main/base.html", {})

def home(response):
    return render(response, "main/home.html", {})

def profile(response):
    return render(response, "main/profile.html", {})

def facilities(response):
    return render(response, "main/facilities.html", {})

def reservations(response):
    return render(response, "main/reservations.html", {})

def profile(response):
    student = Student.objects.all()
    return render(response, "main/profile.html", {'student': student})