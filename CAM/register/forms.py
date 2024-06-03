from django import forms
from main.models import Student, Staff
from django.contrib.auth.forms import AuthenticationForm


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_id', 'name', 'email', 'password']
    
    student_id = forms.CharField(label='Student ID', max_length=100)
    name = forms.CharField(label='Name', max_length=100)
    email = forms.EmailField(label='Email', max_length=100)
    password = forms.CharField(label='Password',widget=forms.PasswordInput)
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
    
    
class StaffForm(forms.ModelForm):
    class Meta:
        model = Staff
        fields = ['staff_id', 'name', 'email', 'password']
    
    staff_id = forms.CharField(label='Staff ID', max_length=100)
    name = forms.CharField(label='Name', max_length=100)
    email = forms.EmailField(label='Email', max_length=100)
    password = forms.CharField(label='Password',widget=forms.PasswordInput)
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

    
class LoginAuthForm(AuthenticationForm):
    username = forms.CharField(label='Student/Staff ID', max_length=100)
    password = forms.CharField(label='Password',widget=forms.PasswordInput)
    



