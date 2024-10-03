from django.contrib import admin
from .models import Course

class CourseAdmin(admin.ModelAdmin):
    list_display = ('course_name',)

admin.site.register(Course, CourseAdmin)