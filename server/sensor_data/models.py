from django.db import models
from users.models import Patient

class MeasurementType(models.Model):
    type = models.CharField(max_length=20)
    max_range = models.FloatField()
    min_range = models.FloatField()

    def __str__(self):
        return self.type


class SingleRecord(models.Model):
    sensor_data = models.ForeignKey('SensorData', related_name='records', on_delete=models.CASCADE)
    type = models.ForeignKey(MeasurementType, related_name="records", on_delete=models.CASCADE)
    value = models.FloatField()

class SensorData(models.Model):
    patient = models.ForeignKey(Patient, related_name="sensor_data", on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)