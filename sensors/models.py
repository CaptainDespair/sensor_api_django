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

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'<Sensor {self.name}>'


class Event(models.Model):

    id = models.AutoField(
        primary_key=True
    )

    sensor_id = models.ForeignKey(
        Sensor, on_delete=models.CASCADE, related_name='events'
    )

    name = models.CharField(
        max_length=255,
    )

    temperature = models.IntegerField(null=True)

    humidity = models.IntegerField(null=True)

    def __str__(self):
        return self.name

    def __repr__(self):
        return f'<Event {self.name}>'
