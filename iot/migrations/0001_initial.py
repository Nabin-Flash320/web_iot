# Generated by Django 4.1 on 2023-07-23 14:59

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="IOTModel",
            fields=[
                (
                    "sensor_device_id",
                    models.PositiveIntegerField(primary_key=True, serialize=False),
                ),
                ("sensor_name", models.CharField(max_length=200)),
                ("sensor_itf_type", models.CharField(max_length=100)),
                ("sensor_value_data_type", models.CharField(max_length=100)),
                ("sensor_value_type", models.CharField(max_length=100)),
                ("sensor_value_unit", models.CharField(max_length=100)),
                ("sensor_value", models.CharField(max_length=100)),
                ("sensor_update_time", models.DateField()),
            ],
        ),
    ]
