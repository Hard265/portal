from django.db import models
from django.conf import settings

class TuitionFee(models.Model):
    student = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='tuition_fees')
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    semester = models.CharField(max_length=20)  # e.g., "Fall 2024", "Spring 2025"
    due_date = models.DateField()

    def __str__(self):
        return f"{self.student.reg_number} - {self.semester} - ${self.amount}"

    class Meta:
        ordering = ['-due_date']
