from django.db import models

class UserData(models.Model):
    full_name = models.CharField(max_length=40)
    email = models.EmailField()
    username = models.CharField(max_length=50)
    password = models.CharField(max_length=100)

    def __str__(self):
        return self.username