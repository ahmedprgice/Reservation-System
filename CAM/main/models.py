from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission
# Create your models here.
class Student(AbstractUser ):
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

    def __str__(self):
        return self.name
    
class Reservation(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    date = models.DateField()
    time = models.TimeField()
    duration = models.IntegerField()
    status = models.CharField(max_length=200)

    def __str__(self):
        return self.student.name + ' ' + self.staff.name + ' ' + str(self.date) + ' ' + str(self.time) + ' ' + str(self.duration) + ' ' + self.status

class Reviews(models.Model):
    review_id = models.CharField(max_length=200)
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    staff = models.ForeignKey(Staff, on_delete=models.CASCADE)
    review = models.TextField()
    rating = models.IntegerField()

    def __str__(self):
        return self.student.name + ' ' + self.staff.name + ' ' + self.review + ' ' + str(self.rating)
    
class Facility(models.Model):
    facility_id = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    anemity = models.CharField(max_length=200)
    capacity = models.IntegerField()
    reservations = models.ManyToManyField(Reservation)
    reviews = models.ManyToManyField(Reviews)
    image = models.ImageField(upload_to='facility_pics', blank=True)

    def __str__(self):
        return self.name
    
class Facaulty(models.Model):
    faculty_id = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    facilities = models.ManyToManyField(Facility)
    department = models.CharField(max_length=200)
    image = models.ImageField(upload_to='faculty_pics', blank=True)

    def __str__(self):
        return self.name
    
class AssetManager(models.Model):
    asset_manager_id = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=200)

    def __str__(self):
        return self.name