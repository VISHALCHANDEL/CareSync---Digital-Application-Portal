from django.db import models

class Department(models.Model):
    name = models.CharField(max_length=100, unique=True)
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name


class Hospital(models.Model):
    name = models.CharField(max_length=200)
    registration_number = models.CharField(max_length=100, unique=True)
    hospital_type = models.CharField(
        max_length=100,
        choices=[
            ('Government', 'Government'),
            ('Private', 'Private'),
            ('Trust', 'Trust'),
        ]
    )
    address = models.TextField()
    city = models.CharField(max_length=100)
    state = models.CharField(max_length=100)
    pincode = models.CharField(max_length=10)
    contact_number = models.CharField(max_length=15)
    email = models.EmailField(unique=True)
    website = models.URLField(blank=True, null=True)
    established_year = models.PositiveIntegerField(blank=True, null=True)
    total_beds = models.PositiveIntegerField(default=0)
    emergency_services = models.BooleanField(default=False)
    departments = models.ManyToManyField(Department, related_name='hospitals')
    registration_date = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.name} ({self.city})"
