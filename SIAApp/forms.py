from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['name', 'password', 'confirmPassword', 'email', 'gender', 'birth_date', 'class_stream','class_year', 'usertype']