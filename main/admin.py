from django.contrib import admin
from .models import Student, Staff, Reservation, Reviews, Facility, Facaulty
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'name', 'email', 'password', 'profile_pic')
    search_fields = ('student_id', 'name', 'email', 'password' , 'profile_pic')
    list_filter = ('student_id', 'name', 'email', 'password' , 'profile_pic')


class StaffAdmin(admin.ModelAdmin):
    list_display = ('staff_id', 'name', 'email', 'password' , 'profile_pic')
    search_fields = ('staff_id', 'name', 'email', 'password' , 'profile_pic')
    list_filter = ('staff_id', 'name', 'email', 'password' , 'profile_pic')

admin.site.register(Student, StudentAdmin)
admin.site.register(Staff, StaffAdmin)
admin.site.register(Reservation)
admin.site.register(Reviews)
admin.site.register(Facility)
admin.site.register(Facaulty)

