from django.shortcuts import render
from django.http import HttpResponse
from .models import UserData
import re

def user_form_view(request):
    if request.method == "POST":
        full_name = request.POST.get("full_name")
        email = request.POST.get("email")
        username = request.POST.get("username")
        password = request.POST.get("password")

        # 1. Full name length check
        if len(full_name) > 40:
            return HttpResponse("Full name must be up to 40 characters")

        # 2. Email validation
        email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(email_pattern, email):
            return HttpResponse("Invalid Email Address")

        # 3. Username must start with string followed by number
        username_pattern = r'^[A-Za-z]+\d+$'
        if not re.match(username_pattern, username):
            return HttpResponse("Username must start with letters followed by numbers")

        # 4. Password length check
        if len(password) <= 8:
            return HttpResponse("Password must be more than 8 characters")

        # If all valid → save
        UserData.objects.create(
            full_name=full_name,
            email=email,
            username=username,
            password=password
        )

        return HttpResponse("Data Saved Successfully")

    return render(request, "user_form.html")