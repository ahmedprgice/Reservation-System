from django.contrib import admin
from .models import Student, Staff, Reservation, Reviews, Facility
# Register your models here.

class StudentAdmin(admin.ModelAdmin):
    list_display = ('student_id', 'name', 'email', 'password', 'profile_pic')
    search_fields = ('student_id', 'name', 'email', 'password' , 'profile_pic')
    list_filter = ('student_id', 'name', 'email', 'password' , 'profile_pic')


class StaffAdmin(admin.ModelAdmin):
    list_display = ('staff_id', 'name', 'email', 'password' , 'profile_pic')
    search_fields = ('staff_id', 'name', 'email', 'password' , 'profile_pic')
    list_filter = ('staff_id', 'name', 'email', 'password' , 'profile_pic')

class ReservationAdmin(admin.ModelAdmin):
    list_display = ('class_code', 'date', 'time', 'end_time', 'student_name', 'student_id', 'staff_name','staff_id', 'is_student', 'is_staff')
    def student_name(self, obj):
        return obj.student.name if obj.student else None

    def student_id(self, obj):
        return obj.student.student_id if obj.student else None

    def staff_name(self, obj):
        return obj.staff.name if obj.staff else None

    def staff_id(self, obj):
        return obj.staff.staff_id if obj.staff else None

    def is_student(self, obj):
        return bool(obj.student)

    def is_staff(self, obj):
        return bool(obj.staff)

    student_name.short_description = 'Student Name'
    student_id.short_description = 'Student ID'
    staff_name.short_description = 'Staff Name'
    staff_id.short_description = 'Staff ID'

class FacilityAdmin(admin.ModelAdmin):
    list_display = ('facility_id', 'name', 'anemity', 'capacity', 'image')
    search_fields = ('facility_id', 'name', 'anemity', 'capacity', 'image')
    list_filter = ('facility_id', 'name', 'anemity', 'capacity', 'image')

class ReviewsAdmin(admin.ModelAdmin):
    list_display = ('review_id', 'rating', 'review', 'student_id','staff_id', 'facility' ,'facility_class_code')
    
    def student_id(self, obj):
        return obj.student.student_id if obj.student else None

    def staff_id(self, obj):
        return obj.staff.staff_id if obj.staff else None

admin.site.register(Student, StudentAdmin)
admin.site.register(Staff, StaffAdmin)
admin.site.register(Reservation, ReservationAdmin)
admin.site.register(Reviews, ReviewsAdmin)
admin.site.register(Facility, FacilityAdmin)



