from django.db import models
from django.contrib.auth.models import BaseUserManager, AbstractBaseUser, PermissionsMixin
from django.db.models.signals import post_save
from django.dispatch import receiver

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
        user.is_staff = True
        user.is_superuser = True
        user.save(using=self._db)
        return user


class Student(AbstractBaseUser, PermissionsMixin):
    reg_number = models.CharField(max_length=20, unique=True)
    is_active = models.BooleanField(default=True)
    is_staff = models.BooleanField(default=False)
    is_superuser = models.BooleanField(default=False)

    USERNAME_FIELD = 'reg_number'

    objects = StudentManager()

    def __str__(self):
        return f"{self.reg_number}"


class StudentProfile(models.Model):
    user = models.OneToOneField(Student, on_delete=models.CASCADE, related_name='student_profile')
    name = models.CharField(max_length=100, blank=True)
    email = models.EmailField(blank=True, null=True)
    date_of_birth = models.DateField(null=True, blank=True)
    address = models.TextField(blank=True)
    phone_number = models.CharField(max_length=15, blank=True)

    def __str__(self):
        return f"Profile of {self.user.reg_number}"




@receiver(post_save, sender=Student)
def create_or_update_student_profile(sender, instance, created, **kwargs):
    if created:
            StudentProfile.objects.create(user=instance)
    instance.student_profile.save()
