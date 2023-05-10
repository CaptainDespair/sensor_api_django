from django.db import models
from django.core.validators import MaxValueValidator, MinValueValidator


class Sensor(models.Model):

    id = models.AutoField(
        primary_key=True
    )

    name = models.CharField(
        max_length=255,
    )

    type = models.IntegerField(
        validators=[
            MaxValueValidator(3),
            MinValueValidator(1)
        ]
    )

    def __init__(self, name, type):
        self.name = name
        self.type = type

    def __repr__(self):
        return f'<Sensor {self.name}>'


class Event(models.Model):

    id = models.AutoField(
        primary_key=True
    )

    sensor_id = models.ForeignKey(
        Sensor, on_delete=models.CASCADE
    )

    name = models.CharField(
        max_length=255,
    )

    temperature = models.IntegerField(
        max_length=255,
    )

    humidity = models.IntegerField(
        max_length=255,
    )

    def __init__(self, sensor_id, name, temperature, humidity):
        self.sensor_id = sensor_id
        self.name = name
        self.temperature = temperature
        self.humidity = humidity

    def __repr__(self):
        return f'<Event {self.name}>'
