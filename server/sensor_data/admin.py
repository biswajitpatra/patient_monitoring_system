from django.contrib import admin

from sensor_data.models import MeasurementType, Record, SensorData

admin.site.register(MeasurementType)

class RecordInline(admin.TabularInline):
    model = Record
class SensorDataAdmin(admin.ModelAdmin):
    inlines = (RecordInline, )

admin.site.register(SensorData, SensorDataAdmin)