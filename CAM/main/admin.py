from django.contrib import admin
from .models import Student, Staff, Reservation, Reviews, Facility, Facaulty
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'name', 'email', 'password')
    search_fields = ('student_id', 'name', 'email', 'password')
    list_filter = ('student_id', 'name', 'email', 'password')


class StaffAdmin(admin.ModelAdmin):
    list_display = ('staff_id', 'name', 'email', 'password')
    search_fields = ('staff_id', 'name', 'email', 'password')
    list_filter = ('staff_id', 'name', 'email', 'password')

admin.site.register(Student, StudentAdmin)
admin.site.register(Staff, StaffAdmin)
admin.site.register(Reservation)
admin.site.register(Reviews)
admin.site.register(Facility)
admin.site.register(Facaulty)

