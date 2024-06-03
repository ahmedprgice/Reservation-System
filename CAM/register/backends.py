from django.contrib.auth.backends import BaseBackend
from main.models import Student

class StudentBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        try:
            student = Student.objects.get(name=username)
            if student.password == password:
                return student
            elif student.check_password(password):#if password is hashed
                return student
        except Student.DoesNotExist:
            return None

    def get_user(self, student_id):
        try:
            return Student.objects.get(pk=student_id)
        except Student.DoesNotExist:
            return None
