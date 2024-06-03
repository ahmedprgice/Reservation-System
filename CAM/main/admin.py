from django.contrib import admin
from .models import Student, Staff, Reservation, Reviews, Facility, Facaulty
# Register your models here.

admin.site.register(Student)
admin.site.register(Staff)
admin.site.register(Reservation)
admin.site.register(Reviews)
admin.site.register(Facility)
admin.site.register(Facaulty)

