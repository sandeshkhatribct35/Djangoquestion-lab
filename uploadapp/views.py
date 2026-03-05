from django.shortcuts import render
from django.http import HttpResponse
from .models import UploadedFile

def file_upload_view(request):
    if request.method == 'POST':
        uploaded_file = request.FILES.get('file')

        if not uploaded_file:
            return HttpResponse("No file selected")

        # 1️⃣ Validate Extension
        allowed_extensions = ['jpg', 'jpeg', 'png', 'gif']
        file_extension = uploaded_file.name.split('.')[-1].lower()

        if file_extension not in allowed_extensions:
            return HttpResponse("Only image files (jpg, jpeg, png, gif) are allowed")

        # 2️⃣ Validate File Size (< 2MB)
        if uploaded_file.size > 2 * 1024 * 1024:
            return HttpResponse("File size must be less than 2MB")

        # If valid → Save
        UploadedFile.objects.create(file=uploaded_file)

        return HttpResponse("File uploaded successfully")

    return render(request, "file_upload.html")