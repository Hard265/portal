from django.shortcuts import render
from django.contrib.auth.decorators import login_required


@login_required(login_url="login")
def dashboard(request):
        
    context = {"profile": request.user.student_profile, "user": request.user, "courses": request.user.courses.all()}
    return render(request, "dashboard.html", context)
