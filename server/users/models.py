from django.db import models
from django.contrib.auth.models import User

# Doctor/Caretaker model
class Doctor(models.Model):
    user = models.OneToOneField(User, related_name="doctor", on_delete=models.CASCADE)


# Patient model
class Patient(models.Model):
     user = models.OneToOneField(User, related_name="patient", on_delete=models.CASCADE)
     doctors = models.ManyToManyField(Doctor, related_name="patients",null=True)