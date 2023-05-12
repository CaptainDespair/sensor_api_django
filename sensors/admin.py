from django.contrib import admin

from .models import Sensor, Event

admin.site.register(Sensor)
admin.site.register(Event)
