from django.contrib import admin

from sensor_data.models import MeasurementType, SingleRecord, SensorData

admin.site.register(MeasurementType)
admin.site.register(SingleRecord)
admin.site.register(SensorData)