from typing import Any
from django import forms
from main.models import Student, Staff
from django.contrib.auth.forms import AuthenticationForm, UserChangeForm
from django.core.validators import RegexValidator



class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_id', 'name', 'email', 'password']
    
    student_id = forms.CharField(label='Student ID', max_length=100)
    name = forms.CharField(label='Name', max_length=100)
    email = forms.EmailField(label='Email', max_length=100)
    password = forms.CharField(label='Password',widget=forms.PasswordInput ,required=True, min_length=8, max_length=16)
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Student.objects.filter(email=email).exists():
            raise forms.ValidationError('Email is already taken')
        return email
    
    def save(self, commit=True):
        student = super(StudentForm, self).save(commit=False)
        student.password = self.cleaned_data['password']
       
        if commit:
            student.save()
        return student
   
    def clean_student_id(self):
        student_id = self.cleaned_data.get('student_id')
        if Student.objects.filter(student_id=student_id).exists():
            raise forms.ValidationError('Student ID is already taken')
        return student_id
    
    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise forms.ValidationError('Password must be at least 8 characters')
        if password.isnumeric():
            raise forms.ValidationError('Password must contain at least one letter')
        if not any(char.isdigit() for char in password):
            raise forms.ValidationError('Password must contain at least one number')
        if not any(char.isalpha() for char in password):
            raise forms.ValidationError('Password must contain at least one uppercase letter')
        return password

    
class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['staff_id', 'name', 'email', 'password']
    
    staff_id = forms.CharField(label='Staff ID', max_length=100)
    name = forms.CharField(label='Name', max_length=100)
    email = forms.EmailField(label='Email', max_length=100)
    password = forms.CharField(label='Password',widget=forms.PasswordInput,required=True, min_length=8, max_length=16)
    def clean_email(self):
        email = self.cleaned_data.get('email')
        if Staff.objects.filter(email=email).exists():
            raise forms.ValidationError('Email is already taken')
        return email
    
    def save(self, commit=True):
        staff = super(StaffForm, self).save(commit=False)
        staff.password = self.cleaned_data['password']

        if commit:
            staff.save()
        return staff
    
    def clean_staff_id(self):
        staff_id = self.cleaned_data.get('staff_id')
        if Staff.objects.filter(staff_id=staff_id).exists():
            raise forms.ValidationError('Staff ID is already taken')
        return staff_id
    
    def clean_password(self):
        password = self.cleaned_data.get('password')
        if len(password) < 8:
            raise forms.ValidationError('Password must be at least 8 characters')
        if password.isnumeric():
            raise forms.ValidationError('Password must contain at least one letter')
        if not any(char.isdigit() for char in password):
            raise forms.ValidationError('Password must contain at least one number')
        if not any(char.isalpha() for char in password):
            raise forms.ValidationError('Password must contain at least one uppercase letter')
        return password
    
class LoginAuthForm(AuthenticationForm):
    username = forms.CharField(label='Student/Staff ID', max_length=100)
    password = forms.CharField(label='Password',widget=forms.PasswordInput)
    

