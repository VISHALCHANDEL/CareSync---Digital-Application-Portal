from django.db import models

class Doctor(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField(unique=True)
    specialization = models.CharField(max_length=100, blank=True)
    password = models.CharField(max_length=256)  # hashed password

    def __str__(self):
        return self.name
