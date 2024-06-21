from django.db import models
from django.contrib.auth.models import AbstractUser, Group, Permission

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
class Reservation(models.Model):
    class_code = models.CharField(max_length=10, default='')
    date = models.DateField()
    time = models.TimeField()
    end_time = models.TimeField()  # Add this field
    guests = models.IntegerField()
    special_requests = models.TextField(blank=True)
    is_cancelled = models.BooleanField(default=False)
    student = models.ForeignKey(Student, null=True, blank=True, on_delete=models.SET_NULL)
    staff = models.ForeignKey(Staff, null=True, blank=True, on_delete=models.SET_NULL)

    def __str__(self):
        return f"{self.class_code} on {self.date} from {self.time} to {self.end_time}"

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
