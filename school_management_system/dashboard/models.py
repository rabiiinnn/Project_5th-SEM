# dashboard/models.py

from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    enrollment_number = models.CharField(max_length=20, unique=True)
    date_of_birth = models.DateField()
    grade = models.CharField(max_length=50)
    is_active = models.BooleanField(default=True)
    date_enrolled = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.enrollment_number})"
