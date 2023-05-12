from django_filters import rest_framework as filter
from sensors.models import Event
from sensors_api.settings import UPLOAD_FILE

import json


class EventFilter(filter.FilterSet):
    temperature_value = filter.Filter(field_name='temperature')
    temperature = filter.RangeFilter(field_name='temperature')

    humidity_value = filter.Filter(field_name='humidity')
    humidity = filter.RangeFilter(field_name='humidity')

    class Meta:
        model = Event
        fields = ['temperature',
                  'humidity',
                  'temperature_value',
                  'humidity_value']


def readJsonEvents():
    with open(UPLOAD_FILE) as f:
        data = json.load(f)
    return data
