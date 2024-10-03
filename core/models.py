from django.conf import settings
from django.db import models

from accounts.models import Student

class TuitionFee(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tuition_fees')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    semester = models.CharField(max_length=20)  # e.g., "Fall 2024", "Spring 2025"
    due_date = models.DateField()

    def __str__(self):
        return f"{self.student.reg_number} - {self.semester} - ${self.amount}"

    class Meta:
        ordering = ['-due_date']


class Course(models.Model):
    student = models.ManyToManyField(Student, related_name='courses')
    course_name = models.CharField(max_length=100)

    def __str__(self):
        return self.course_name


class ExaminationResult(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    score = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.student.name} - {self.course.course_name} - {self.score}"