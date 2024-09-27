from django.contrib import admin
from .models import StudentProfile, Student

admin.site.register(Student)
admin.site.register(StudentProfile)
