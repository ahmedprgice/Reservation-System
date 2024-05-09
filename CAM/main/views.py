from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(response):
    return render(response, "main/base.html", {})

def home(response):
    return render(response, "main/home.html", {})

def facilities(response):
    return render(response, "main/facilities.html", {})

def reservations(response):
    return render(response, "main/reservations.html", {})