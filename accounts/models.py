from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser

class StudentManager(BaseUserManager):
    def create_user(self, reg_number, password=None):
        if not reg_number:
            raise ValueError("Students must have a registration number")

        user = self.model(reg_number=reg_number)
        user.set_password(password)
        user.save(using=self._db)
        return user

    def create_superuser(self, reg_number, password=None):
        user = self.create_user(reg_number, password)
        user.is_admin = True
        user.save(using=self._db)
        return user


class Student(AbstractBaseUser):
    reg_number = models.CharField(max_length=20, unique=True)
    name = models.CharField(max_length=100)
    email = models.EmailField()
    is_active = models.BooleanField(default=True)
    is_admin = models.BooleanField(default=False)

    USERNAME_FIELD = 'reg_number'

    objects = StudentManager()

    def __str__(self):
        return self.name


class StudentProfile(models.Model):
    user = models.OneToOneField(Student, on_delete=models.CASCADE, related_name='student_profile')
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.TextField(blank=True)
    phone_number = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return f"Profile of {self.user.reg_number}"

class Course(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course_name = models.CharField(max_length=100)

    def __str__(self):
        return self.course_name


class FeeStatus(models.Model):
    student = models.OneToOneField(Student, on_delete=models.CASCADE)
    amount_due = models.DecimalField(max_digits=8, decimal_places=2)
    due_date = models.DateField()

    def __str__(self):
        return f"{self.student.name} - {self.course.amount_due}"


class ExaminationResult(models.Model):
    student = models.ForeignKey(Student, on_delete=models.CASCADE)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
    score = models.DecimalField(max_digits=5, decimal_places=2)

    def __str__(self):
        return f"{self.student.name} - {self.course.course_name} - {self.score}"


@receiver(post_save, sender=Student)
def create_or_update_student_profile(sender, instance, created):
    if created:
            StudentProfile.objects.create(user=instance)
    instance.student_profile.save()
