from django import forms
from django.contrib.auth.forms import PasswordChangeForm, UserChangeForm
from main.models import Student, Staff

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


class ChangePasswordForm(PasswordChangeForm):
    def __init__(self, *args, **kwargs):
        super(ChangePasswordForm, self).__init__(*args, **kwargs)
        self.fields['old_password'].help_text = None
        self.fields['new_password1'].help_text = None
        self.fields['new_password2'].help_text = None
