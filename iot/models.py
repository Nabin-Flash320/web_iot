from django.db import models

# Create your models here.
class IOTModel(models.Model):
    sensor_device_id = models.PositiveIntegerField(primary_key=True)
    sensor_name = models.CharField(max_length=200)
    sensor_itf_type = models.CharField(max_length=100)
    sensor_value_data_type = models.CharField(max_length=100)
    sensor_value_type = models.CharField(max_length=100)
    sensor_value_unit = models.CharField(max_length=100)
    sensor_value = models.CharField(max_length=100)
    sensor_update_time = models.DateField()

    def meta():
        ordering = ("sensor_device_id", "sensor_name", "sensor_itf_type", "sensor_value_data_type", "sensor_value_type", 
                    "sensor_value_unit", "sensor_value", "sensor_update_time")

    def __str__(self):
        return f"{self.sensor_device_id}, {self.sensor_name}, {self.sensor_itf_type}, {self.sensor_value_data_type}, \
                    {self.sensor_value_type}, {self.sensor_value_unit}, {self.sensor_value}, {self.sensor_update_time}"
