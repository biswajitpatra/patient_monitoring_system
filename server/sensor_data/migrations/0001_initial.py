# Generated by Django 3.2.3 on 2021-05-22 08:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('users', '0002_alter_doctor_user'),
    ]

    operations = [
        migrations.CreateModel(
            name='MeasurementType',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=20)),
                ('max_range', models.FloatField()),
                ('min_range', models.FloatField()),
            ],
        ),
        migrations.CreateModel(
            name='SensorData',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('value', models.FloatField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('patient', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='users.patient')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='sensor_data.measurementtype')),
            ],
        ),
    ]
