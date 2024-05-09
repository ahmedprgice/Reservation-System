from django.db import models

# Create your models here.
class Student(models.Model):
    student_id = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=200)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

    def __str__(self):
        return self.name
    
class Staff(models.Model):
    staff_id = models.CharField(max_length=200)
    name = models.CharField(max_length=200)
    email = models.EmailField()
    password = models.CharField(max_length=200)
    profile_pic = models.ImageField(upload_to='profile_pics', blank=True)

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