from django.db import models

class ProjectSubmission(models.Model):
    registration_number = models.CharField(max_length=100)
    email = models.EmailField()
    project_file = models.FileField(upload_to='projects/')

    def __str__(self):
        return self.registration_number