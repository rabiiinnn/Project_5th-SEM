# dashboard/urls.py
from django.urls import path
from .views import StudentList

urlpatterns = [
    path('api/students/', StudentList.as_view(), name='student-list'),
]
