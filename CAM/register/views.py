from django.shortcuts import render, redirect
from .forms import StudentForm, StaffForm, LoginForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
# Create your views here.

def student_register(response):
    if response.method == "POST":
        form = StudentForm(response.POST, response.FILES)
        if form.is_valid():
            form.save()
        
        return redirect("/home")
    else:
        form = StudentForm()

    return render(response, "register/register.html", {"form":form})

def user_login(response):
    if response.method == "POST":
        form = AuthenticationForm(response, data=response.POST)
        if form.is_valid():
            username = form.cleaned_data['username']
            password = form.cleaned_data['password']
            user = authenticate(response, username=username, password=password)
            if user is not None:
                login(response, user)
                messages.success(response, 'You are now logged in')
                return redirect("/home")
            else:
                messages.error(response, 'Invalid username or password')
    else:
        form = AuthenticationForm()
    return render(response, "register/login.html", {"form":form})
    
# def staff_register(response):
#     if response.method == "POST":
#         form = StaffForm(response.POST, response.FILES)
#         if form.is_valid():
#             form.save()
        
#         return redirect("/home")
#     else:
#         form = StaffForm()

#     return render(response, "register/staff_register.html", {"form":form})