from django.db import models

class Patient(models.Model):
    name = models.CharField(max_length=100)
    patient_id = models.CharField(max_length=50)
    mobile = models.CharField(max_length=10)
    gender = models.CharField(max_length=10)
    address = models.TextField(blank=True)
    dob = models.DateField()
    doctor_name = models.CharField(max_length=100)

    def __str__(self):
        return self.name