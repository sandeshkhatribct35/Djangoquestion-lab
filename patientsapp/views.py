from django.shortcuts import render
from .forms import PatientForm

def patient_form_view(request):
    if request.method == 'POST':
        form = PatientForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, 'success.html')
    else:
        form = PatientForm()

    return render(request, 'patient_form.html', {'form': form})