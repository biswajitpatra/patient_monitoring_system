from django.db import models
from users.models import Patient
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError


class MeasurementType(models.Model):
    type = models.CharField(max_length=20)
    max_range = models.FloatField()
    min_range = models.FloatField()

    def __str__(self):
        return self.type

    def clean(self):
        if self.max_range <= self.min_range:
            raise ValidationError(
                {
                    "min_range": ValidationError(
                        "'min_range' should be smaller than 'max_range'"
                    ),
                    "max_range": ValidationError(
                        "'max_range' should be greater than 'min_range'"
                    ),
                }
            )


class Record(models.Model):
    sensor_data = models.ForeignKey(
        "SensorData", related_name="records", on_delete=models.CASCADE
    )
    measurement_type = models.ForeignKey(
        MeasurementType, related_name="records", on_delete=models.CASCADE
    )
    value = models.FloatField()

    def __str__(self):
        return f"{self.measurement_type.type} <{self.value}>"

    @property
    def owners(self):
        return self.sensor_data.owners


class SensorData(models.Model):
    patient = models.ForeignKey(
        Patient, related_name="sensor_data", on_delete=models.CASCADE
    )
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.patient.user.username

    @property
    def owners(self):
        return [self.patient.user, User.objects.get(doctor__patients=self.patient)]

    class Meta:
        verbose_name_plural = "Sensor Data"
