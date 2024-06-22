# from django.shortcuts import render
# from .models import Student, Staff, Reservation, Reviews, Facility
# from django.contrib.auth.decorators import login_required
# from .forms import ProfileForm, ChangePasswordForm
# from django.contrib.auth import update_session_auth_hash
# from django.contrib import messages
# from django.shortcuts import redirect
# from django.contrib.auth import login
# from django.shortcuts import render, redirect
# from .models import Reservation
# from .forms import ReservationForm
# from django.shortcuts import render, redirect, get_object_or_404
# from .models import Reservation
# from django.shortcuts import render, redirect, get_object_or_404
# from django.contrib.auth.decorators import login_required
# from .forms import ReservationForm
# from .models import Reservation

from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import update_session_auth_hash, login
from django.contrib import messages
from .models import Student, Staff, Reservation, Reviews, Facility
from .forms import ProfileForm, ChangePasswordForm, ReservationForm, ReviewForm  
from django.db.models import Avg, Count
import logging

logger = logging.getLogger(__name__)

# Create your views here.

def index(response):
    return render(response, "main/base.html", {})

def home(response):
    return render(response, "main/home.html", {})


def facilities(request):
    facilities = Facility.objects.all()

    for facility in facilities:
        reviews = Reviews.objects.filter(facility=facility)
        logger.info(f"Facility1: {facility.name}, Number of reviews: {reviews.count()}")

        average_rating = reviews.aggregate(Avg('rating'))['rating__avg']
        facility.average_rating = round(average_rating, 1) if average_rating else None
    

    return render(request, "main/facilities.html", {"facilities": facilities})

def facility_anemity(request, facility_anemity):
    template_mapping = {
        'classes': 'main/classes.html',
        'labs': 'main/labs.html',
        'sportfacilities': 'main/sportfacilites.html',
        'privaterooms': 'main/privaterooms.html',
    }
    if facility_anemity in template_mapping:
        facilities = Facility.objects.filter(anemity=facility_anemity)

        for facility in facilities:
            reviews = Reviews.objects.filter(facility=facility)
            logger.info(f"Facility: {facility.name}, Number of reviews: {reviews.count()}")
            average_rating = reviews.aggregate(Avg('rating'))['rating__avg']
            facility.average_rating = round(average_rating, 1) if average_rating else None
            logger.info(f"Facility: {facility.name}, Average rating: {facility.average_rating}")

        template = template_mapping[facility_anemity]
    else:
        facilities = Facility.objects.all()
        template = 'main/home.html'  # Default template
    
    return render(request, template,{"facilities": facilities})



@login_required(login_url='/login/')
@login_required(login_url='/login/')
def reservations(request):
    facilities = Facility.objects.all()

    for facility in facilities:
        reviews = Reviews.objects.filter(facility=facility)
        logger.info(f"Facility1: {facility.facility_id }")

        average_rating = reviews.aggregate(Avg('rating'))['rating__avg']
        facility.average_rating = round(average_rating, 1) if average_rating else None

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

    return render(request, 'main/reservations.html', {'form': form, 'reservations': reservations ,"facilities": facilities})

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

def reviews(response):
    reviews = Reviews.objects.all()
    return render(response, "main/reviews.html", {"reviews":reviews})

# @login_required
# def addreview(request, reservation_id):
#     reservation  = get_object_or_404(Reservation, pk=reservation_id)

#     if request.method == 'POST':
#         form = ReviewForm(request.POST)
#         if form.is_valid():
#             review = form.save(commit=False)
#             review.student = request.user  # Assuming the current user is the student
#             review.facility_code = reservation.facility  # Assuming Reservation has a facility attribute
#             review.save()
#             # Optionally, you can add a confirmation message or redirect to a different page
#             return redirect('reviews')
#     else:
#         form = ReviewForm()

#     context = {
#             'form': form,
#             'reservation': reservation,
#         }

#     return render(request, "main/addreview.html", context)
@login_required
def add_review(request, facility_id):
    facility = get_object_or_404(Facility, pk=facility_id)
    
    if request.method == 'POST':
        form = ReviewForm(request.POST, user=request.user)
        if form.is_valid():
            review = form.save(commit=False)
            review.facility = facility
            review.save()
            # Optionally, redirect to a 'success' page or the facility's detail page
            return redirect('reviews')  # Assuming 'reviews' is your redirect name
    else:
        form = ReviewForm()
    
    return render(request, 'main/add_review.html', {'form': form, 'facility': facility})