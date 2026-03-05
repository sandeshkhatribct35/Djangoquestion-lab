from django.db import models

class Appointment(models.Model):
    name = models.CharField(max_length=100)
    gender = models.CharField(max_length=10)
    hobbies = models.CharField(max_length=200)
    appointment_datetime = models.DateTimeField()
    country = models.CharField(max_length=50)
    resume = models.FileField(upload_to='resumes/')
    email = models.EmailField()
    phone = models.CharField(max_length=15)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.name