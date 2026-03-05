from django.shortcuts import render
from django.http import HttpResponse
from .models import ProjectSubmission
import re

def project_upload_view(request):
    if request.method == "POST":
        reg_no = request.POST.get("registration_number")
        email = request.POST.get("email")
        uploaded_file = request.FILES.get("project_file")

        # 1️⃣ Required field validation
        if not reg_no or not email or not uploaded_file:
            return HttpResponse("All fields are mandatory")

        # 2️⃣ Email validation
        email_pattern = r'^[\w\.-]+@[\w\.-]+\.\w+$'
        if not re.match(email_pattern, email):
            return HttpResponse("Invalid email format")

        # 3️⃣ File extension validation
        allowed_extensions = ['pdf', 'doc', 'docx', 'ppt', 'pptx', 'jpeg']
        file_extension = uploaded_file.name.split('.')[-1].lower()

        if file_extension not in allowed_extensions:
            return HttpResponse("Invalid file format")

        # 4️⃣ File size validation (< 5MB)
        if uploaded_file.size > 5 * 1024 * 1024:
            return HttpResponse("File size must be less than 5MB")

        # If all valid → Save
        ProjectSubmission.objects.create(
            registration_number=reg_no,
            email=email,
            project_file=uploaded_file
        )

        return HttpResponse("Project submitted successfully")

    return render(request, "project_form.html")