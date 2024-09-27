from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url="login")
def dashboard(request):
    student = request.user
    profile = student.profile
    # courses = Course.objects.filter(student=student)
    # fees = FeeStatus.objects.filter(student=student)
    # results = ExaminationResult.objects.filter(student=student)
    context = {"profile": profile}
    return render(request, "dashboard.html", context)
