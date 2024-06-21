from django.shortcuts import render
from .models import Student, Staff, Reservation, Reviews, Facility, Facaulty
from django.contrib.auth.decorators import login_required
from .forms import ProfileForm, ChangePasswordForm
from django.contrib.auth import update_session_auth_hash
from django.contrib import messages
from django.shortcuts import redirect
from django.contrib.auth import login
from django.shortcuts import render, redirect
from .models import Reservation
from .forms import ReservationForm
from django.shortcuts import render, redirect, get_object_or_404
from .models import Reservation



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

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from .forms import ReservationForm
from .models import Reservation

@login_required(login_url='/login/')
@login_required(login_url='/login/')
def reservations(request):
    if request.method == 'POST':
        form = ReservationForm(user=request.user, data=request.POST)
        if form.is_valid():
            reservation = form.save(commit=False)
            if hasattr(request.user, 'student_id'):
                reservation.student = request.user
            elif hasattr(request.user, 'staff_id'):
                reservation.staff = request.user
            reservation.save()
            return redirect('reservations')
    else:
        form = ReservationForm(user=request.user)

    if hasattr(request.user, 'student_id'):
        reservations = Reservation.objects.filter(student=request.user)
    elif hasattr(request.user, 'staff_id'):
        reservations = Reservation.objects.filter(staff=request.user)
    else:
        reservations = Reservation.objects.none()

    return render(request, 'main/reservations.html', {'form': form, 'reservations': reservations})

@login_required
def cancel_reservation(request, reservation_id):
    reservation = get_object_or_404(Reservation, pk=reservation_id)
    
    if request.method == 'POST':
        reservation.cancel_reservation()
        # Optionally, you can add a confirmation message or redirect to a different page
        return redirect('reservations')
    
    # Handle GET request or display confirmation message
    return render(request, 'main/cancel_confirmation.html', {'reservation': reservation})


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

@login_required
def change_password(request):
    if hasattr(request.user, 'student_id'):
        user = Student.objects.get(id=request.user.id)
        user_type = "Student"
    elif hasattr(request.user, 'staff_id'):
        user = Staff.objects.get(id=request.user.id)
        user_type = "Staff"
    else:
        messages.error(request, 'User not found')
        return redirect("/home")
    
    if request.method == 'POST':
        form = ChangePasswordForm(user_type, user, request.POST)
        if form.is_valid():
            user.set_password(form.cleaned_data['new_password'])
            user.save()
            backend_path = 'main.backends.StudentBackend' if user_type == "Student" else 'main.backends.StaffBackend'
            login(request, user, backend=backend_path)
        
            messages.success(request, 'Password updated successfully')
            return redirect('/home')
        else:
            messages.error(request, 'Password not updated. Please correct the errors.')
    else:
        form = ChangePasswordForm(user_type,user)
    return render(request, 'main/changepassword.html', {'form': form, 'messages': messages.get_messages(request)})