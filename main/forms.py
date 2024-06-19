from django import forms
from django.contrib.auth.forms import PasswordChangeForm, UserChangeForm
from django.core.validators import RegexValidator
from main.models import Student, Staff
from django import forms
from .models import Reservation

class ProfileForm(UserChangeForm):
    student_id = forms.CharField(label='Student ID', max_length=100, required=False)
    staff_id = forms.CharField(label='Staff ID', max_length=100 , required=False)
    name = forms.CharField(label='Name', max_length=100)
    email = forms.EmailField(label='Email', max_length=100)
    profile_pic = forms.ImageField(label='Profile Picture', required=False)
    
    def __init__(self, *args, **kwargs):
        user = kwargs.pop('user')
        super(ProfileForm,self).__init__(*args, **kwargs)
        self.user = user

        if isinstance(user, Student):
            self.fields['student_id'].initial = user.student_id
            self.fields['staff_id'].widget = forms.HiddenInput()
            self.fields['staff_id'].required = False
            self.fields['student_id'].required = True
        elif isinstance(user, Staff):
            self.fields['staff_id'].initial = user.staff_id
            self.fields['student_id'].widget = forms.HiddenInput()
            self.fields['student_id'].required = False
            self.fields['staff_id'].required = True

        if 'password' in self.fields:
            del self.fields['password']
    class Meta:
        model = Student
        fields =['profile_pic', 'student_id', 'staff_id', 'name', 'email']

def clean_email(self):
    email = self.cleaned_data.get('email')
    if Student.objects.filter(email=email).exists():
        raise forms.ValidationError('Email is already taken')
    return email

def save(self, commit=True):
    user = self.user
    user.email = self.cleaned_data['email']
    user.name = self.cleaned_data['name']
    user.profile_pic = self.cleaned_data['profile_pic']
    
    if isinstance(user, Student):
       user.student_id = self.cleaned_data['student_id'] 
    elif isinstance(user, Staff):
        user.staff_id = self.cleaned_data['staff_id']
    if commit:
        user.save()
    return user

class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(label='Old Password', widget=forms.PasswordInput, required=True, min_length=8, max_length=16)
    new_password = forms.CharField(label='New Password', widget=forms.PasswordInput, required=True, min_length=8, max_length=16)
    confirm_password = forms.CharField(label='Confirm New Password', widget=forms.PasswordInput, required=True, min_length=8, max_length=16)
   
    def __init__(self, user_type, user, *args, **kwargs):
        self.user_type = user_type
        self.user = user
        super().__init__(*args, **kwargs)

    def clean_old_password(self):
        old_password = self.cleaned_data.get('old_password')
        if self.user_type == 'Student':
            self.user = Student.objects.get(id=self.user.id)
        elif self.user_type == 'Staff':
            self.user = Staff.objects.get(id=self.user.id)
        if old_password != self.user.password:
            raise forms.ValidationError('Old password is incorrect')
        return old_password
    
    def clean_new_password(self):
         new_password = self.cleaned_data.get('new_password')
        #  if new_password.isnumeric():
        #     raise forms.ValidationError('Password cannot be entirely number.')
         if not any(char.isdigit() for char in new_password):
                raise forms.ValidationError('Password must contain at least one number.')
         if not any(char.isalpha() for char in new_password):
                raise forms.ValidationError('Password must contain at least one alphabetic.')
         return new_password
    
    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get('new_password')
        confirm_password = cleaned_data.get('confirm_password')
        if new_password and confirm_password and new_password != confirm_password:
            raise forms.ValidationError('New passwords do not match')
        return cleaned_data
    
    def save(self, commit=True):
        new_password = self.cleaned_data['new_password']
        if self.user_type == 'Student':
            self.user.password = new_password
        elif self.user_type == 'Staff':
            self.user.password = new_password
        if commit:
            self.user.save()    
        return self.user


class ReservationForm(forms.ModelForm):
    class Meta:
        model = Reservation
        fields = ['class_code', 'date', 'time', 'guests', 'special_requests']