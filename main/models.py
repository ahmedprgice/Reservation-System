from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
from django.db.models import Avg

class Student(AbstractUser):
    student_id = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=200)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    is_active = models.BooleanField(default=True)
    username = 'student_id'
    
    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        related_name='student_groups',
        related_query_name='student_group',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        related_name='student_user_permissions',
        related_query_name='student_user_permission',
    )

    class Meta:
        verbose_name = 'Student'
        verbose_name_plural = 'Students'

    def is_student(self):
        return True

    def set_password(self, raw_password):
        self.password = raw_password

    def __str__(self):
        return self.name
    
class Staff(AbstractUser):
    staff_id = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=200)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)
    is_active = models.BooleanField(default=True)
    username = 'staff_id'
    
    groups = models.ManyToManyField(
        Group,
        verbose_name='groups',
        blank=True,
        related_name='staff_groups',
        related_query_name='staff_group',
    )
    user_permissions = models.ManyToManyField(
        Permission,
        verbose_name='user permissions',
        blank=True,
        related_name='staff_user_permissions',
        related_query_name='staff_user_permission',
    )

    class Meta:
        verbose_name = 'Staff'
        verbose_name_plural = 'Staffs'

    def is_staff(self):
        return True
    
    def set_password(self, raw_password):
        self.password = raw_password

    def __str__(self):
        return self.name
    
class Reservation(models.Model):
    class_code = models.CharField(max_length=20, default='')
    date = models.DateField()
    time = models.TimeField()
    end_time = models.TimeField()  # Add this field
    guests = models.IntegerField()
    special_requests = models.TextField(blank=True)
    is_cancelled = models.BooleanField(default=False)
    student = models.ForeignKey(Student, null=True, blank=True, on_delete=models.SET_NULL)
    staff = models.ForeignKey(Staff, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return self.class_code

    def cancel_reservation(self):
        self.is_cancelled = True
        self.save()
        self.delete()

    def student_name(self):
        return self.student.name if self.student else None
    
    def staff_name(self):
        return self.staff.name if self.staff else None
    
    def student_id(self):
        return self.student.student_id if self.student else None
    
    def staff_id(self):
        return self.staff.staff_id if self.staff else None
    
    def is_student(self):
        return bool(self.student)
    
    def is_staff(self):
        return bool(self.staff)

    student_name.short_description = 'Student Name'
    student_id.short_description = 'Student ID'
    staff_name.short_description = 'Staff Name'
    staff_id.short_description = 'Staff ID'


    
class Facility(models.Model):
    facility_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=200)
    anemity = models.CharField(max_length=200)
    capacity = models.IntegerField()
    reservations = models.ManyToManyField(Reservation)
    image = models.ImageField(upload_to='facility_pics', blank=True)

    def __str__(self):
        return self.name
    
    def average_rating(self):
        average = self.reviews.aggregate(Avg('rating'))['rating__avg']
        return round(average, 1) if average is not None else None
    
class Reviews(models.Model):
    review_id = models.AutoField(primary_key=True)
    student = models.ForeignKey(Student, null=True, blank=True, on_delete=models.SET_NULL)
    staff = models.ForeignKey(Staff, null=True, blank=True, on_delete=models.SET_NULL)
    review = models.TextField()
    rating = models.IntegerField()
    facility = models.ForeignKey(Facility, on_delete=models.CASCADE, null=True, blank=True)
    facility_class_code = models.CharField(max_length=20, default='')

    def __str__(self):
        return self.review + ' ' + str(self.rating)
    
    def student_id(self):
        return self.student.student_id if self.student else None
    
    def staff_id(self):
        return self.staff.staff_id if self.staff else None
    
    # def add_review(self):
    #     self.save()