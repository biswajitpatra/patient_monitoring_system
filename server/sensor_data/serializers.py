from rest_framework import serializers
from sensor_data.models import Record, SensorData, MeasurementType
from django.core.mail import send_mail


class MeasurementTypeSerializer(serializers.ModelSerializer):
    class Meta:
        model = MeasurementType
        fields = "__all__"


class BasicRecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = ["value", "measurement_type"]


class RecordSerializer(serializers.ModelSerializer):
    class Meta:
        model = Record
        fields = "__all__"


class SensorDataSerializer(serializers.ModelSerializer):
    records = BasicRecordSerializer(many=True)

    class Meta:
        model = SensorData
        fields = "__all__"

    def create(self, validated_data):
        records_data = validated_data.pop("records")
        sensor_data = SensorData.objects.create(**validated_data)
        for record_data in records_data:
            record = Record.objects.create(sensor_data=sensor_data, **record_data)
            
            if not (
                record.measurement_type.min_range
                <= record.value
                <= record.measurement_type.max_range
            ):
                send_mail(
                    subject="ALERT FOR PATIENT",
                    from_email=None,
                    message=f"{sensor_data.patient.user.first_name} has abnormal levels of {record.measurement_type.type} i.e, {record.value}",
                    recipient_list=list(sensor_data.patient.doctors.values_list("user__email",flat=True)),
                )

        return sensor_data
