from django.shortcuts import render, redirect
from .models import Student
from django.http import HttpResponse

def login_view(request):
    if request.method == "POST":
        username = request.POST.get('username')
        password = request.POST.get('password')

        try:
            student = Student.objects.get(username=username, password=password)
            return redirect('dashboard')
        except Student.DoesNotExist:
            return HttpResponse("Invalid username/password")

    return render(request, 'login.html')


def dashboard(request):
    return HttpResponse("Welcome to Dashboard")