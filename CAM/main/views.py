from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def index(response):
    return HttpResponse("Hello, world. You're at the polls index.")

def v1(response):
    return HttpResponse("<h1>Version 1</h1>")