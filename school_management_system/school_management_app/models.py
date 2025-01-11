from django.db import models

class Student(models.Model):
    first_name = models.CharField(max_length=50)
    last_name = models.CharField(max_length=50)
    age = models.PositiveIntegerField()
    email = models.EmailField(unique=True)
    enrollment_number = models.CharField(max_length=15, unique=True)
    date_of_birth = models.DateField()
    grade = models.CharField(max_length=100)
    date_enrolled = models.DateField(auto_now_add=True)
    is_active = models.BooleanField(default=True)
    
    def __str__(self):
        return f"{self.first_name} {self.last_name} - {self.enrollment_number}"
