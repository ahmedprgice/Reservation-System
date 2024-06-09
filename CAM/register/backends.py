from django.contrib.auth.backends import BaseBackend
from main.models import Student, Staff

class LoginBackend(BaseBackend):
    def authenticate(self, request, username=None, password=None):
        try:
            staff = Staff.objects.get(staff_id=username)
            if staff.password == password or staff.check_password(password):#if password is not hashed
                return staff
        except Staff.DoesNotExist:
            pass

    
        try:
            student = Student.objects.get(student_id=username)
            if student.password == password or student.check_password(password):
                return student
        except Student.DoesNotExist:
            pass

        
        return None
    
    def get_user(self, user_id):

            try:
                return Staff.objects.get(pk=user_id)
            except Staff.DoesNotExist:
                try:
                    return Student.objects.get(pk=user_id)
                except Student.DoesNotExist:
                        return None