from django.contrib.auth.backends import BaseBackend
from main.models import Student, Staff

class StudentBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        try:
            user = Student.objects.get(student_id=username)
            if user.check_password(password):
                return user
        except Student.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Student.objects.get(pk=user_id)
        except Student.DoesNotExist:
            return None
        
class StaffBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        try:
            user = Staff.objects.get(staff_id=username)
            if user.check_password(password):
                return user
        except Staff.DoesNotExist:
            return None

    def get_user(self, user_id):
        try:
            return Staff.objects.get(pk=user_id)
        except Staff.DoesNotExist:
            return None