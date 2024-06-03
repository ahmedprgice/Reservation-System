from django import forms
from main.models import Student, Staff


class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['student_id', 'name', 'email', 'password']
    
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

    
class LoginForm(forms.Form):
    name = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)



