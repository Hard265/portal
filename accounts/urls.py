from django.urls import path
from . import views

urlpatterns = [
    path('login', views.student_login, name='login'),
    path('dashboard', views.dashboard, name='dashboard'),
]