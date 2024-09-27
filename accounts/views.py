from django.shortcuts import render, redirect
from django.contrib.auth import authenticate, login


def student_login(request):
    if request.method == "POST":
        reg_number = request.POST.get("reg_number")
        password = request.POST.get("password")
        student = authenticate(reg_number=reg_number, password=password)

        if student is not None:
            login(request, student)
            return redirect("dashboard")
    return render(request, "accounts/login.html")

