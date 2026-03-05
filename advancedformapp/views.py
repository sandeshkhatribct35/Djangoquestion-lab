from django.shortcuts import render
from django.http import HttpResponse
from .models import Appointment
import re
from datetime import datetime

def appointment_form_view(request):
    if request.method == "POST":
        # Get form data
        name = request.POST.get("name")
        gender = request.POST.get("gender")
        hobbies = request.POST.get("hobbies")
        appointment_datetime = request.POST.get("appointment_datetime")
        country = request.POST.get("country")
        email = request.POST.get("email")
        phone = request.POST.get("phone")
        password = request.POST.get("password")
        confirm_password = request.POST.get("confirm_password")
        resume = request.FILES.get("resume")

        # 1️⃣ Required fields
        if not all([name, gender, hobbies, appointment_datetime, country, email, phone, password, confirm_password, resume]):
            return HttpResponse("All fields are required")

        # 2️⃣ Appointment date/time cannot be in past
        try:
            appt_datetime = datetime.strptime(appointment_datetime, "%Y-%m-%dT%H:%M")
            if appt_datetime < datetime.now():
                return HttpResponse("Appointment date cannot be in the past")
        except ValueError:
            return HttpResponse("Invalid appointment date/time format")

        # 3️⃣ Resume validation
        allowed_extensions = ['pdf', 'doc', 'docx', 'jpg', 'jpeg', 'png']
        file_extension = resume.name.split('.')[-1].lower()
        if file_extension not in allowed_extensions:
            return HttpResponse("Resume must be pdf, ms-word or image")
        if resume.size > 2 * 1024 * 1024:
            return HttpResponse("Resume file size must be less than 2MB")

        # 4️⃣ Email validation
        email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(email_pattern, email):
            return HttpResponse("Invalid email format")

        # 5️⃣ Phone number validation (Nepal format)
        if not re.match(r'^(9\d{9}|01\d{7})$', phone):
            return HttpResponse("Invalid phone number format")

        # 6️⃣ Password validation
        password_pattern = r'^(?=.*[a-z])(?=.*[A-Z])(?=.*\d)(?=.*[\W_]).{8,}$'
        if not re.match(password_pattern, password):
            return HttpResponse("Password must be at least 8 chars with uppercase, lowercase, number & symbol")

        if password != confirm_password:
            return HttpResponse("Password and Confirm Password do not match")

        # ✅ Save to database
        Appointment.objects.create(
            name=name,
            gender=gender,
            hobbies=hobbies,
            appointment_datetime=appt_datetime,
            country=country,
            email=email,
            phone=phone,
            password=password,
            resume=resume
        )

        return HttpResponse("Appointment submitted successfully")

    return render(request, "appointment_form.html")