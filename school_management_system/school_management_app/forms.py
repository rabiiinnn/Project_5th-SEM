from django import forms
from .models import Student

class StudentForm(forms.ModelForm):
    class Meta:
        model = Student
        fields = ['first_name', 'last_name', 'age', 'email', 'enrollment_number', 'date_of_birth', 'grade', 'is_active']
