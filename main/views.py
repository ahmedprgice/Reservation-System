from django.shortcuts import render
from .models import Student, Staff, Reservation, Reviews, Facility, Facaulty
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm, ChangePasswordForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import login



# Create your views here.

def index(response):
    return render(response, "main/base.html", {})

def home(response):
    return render(response, "main/home.html", {})

# def profile(response):
#     print(response.user)
#     return render(response, "main/profile.html", {})

def facilities(response):
    return render(response, "main/facilities.html", {})

def reservations(response):
    return render(response, "main/reservations.html", {})

@login_required
def update_profile(request):
    if hasattr(request.user, 'student_id'):
        current_user = Student.objects.get(id=request.user.id)
        user_type = "Student"
        messages.info(request, 'Student')
    elif hasattr(request.user, 'staff_id'):
        current_user = Staff.objects.get(id=request.user.id)
        user_type = "Staff"
        messages.info(request, 'Staff')
    else:
        messages.error(request, 'User not found')
        return redirect("/home")
    
    if request.method == "POST":
        user_form = ProfileForm(request.POST, request.FILES, instance=current_user, user=current_user)
        if user_form.is_valid():
            user_form.save()
            backend_path = 'main.backends.StudentBackend' if user_type == "Student" else 'main.backends.StaffBackend'

            login(request, current_user, backend=backend_path)
            messages.success(request, 'Profile updated successfully')
            messages.error(request, 'Profile not updated')
            return redirect("/home")
    else:
            user_form = ProfileForm(instance=current_user, user=current_user)
            messages.error(request, 'Profile not updated')
    return render(request, "main/profile.html", {"user_form":user_form, "messages": messages.get_messages(request)})

def classes_view(request):
    return render(request, 'main/classes.html')

def labs_view(request):
    return render(request, 'main/labs.html')

def sportfacilites_view(request):
    return render(request, 'main/sportfacilites.html')

def Private_Study_Rooms(request):
    return render(request, 'main/privaterooms.html')

def change_password(request):
    if request.method == 'POST':
        passform = ChangePasswordForm(request.user, request.POST)
        if passform.is_valid():
            user = passform.save()
            update_session_auth_hash(request, user)#prevent user from being logged out
            messages.success(request, 'Password updated successfully')
            return redirect('/profile')
        else:
            messages.error(request, 'Password not updated')
    else:
        passform = ChangePasswordForm(request.user)
    return render(request, 'main/changepassword.html',{'passform': passform, 'messages': messages.get_messages(request)})