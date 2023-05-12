from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.exceptions import NotFound
from rest_framework.pagination import PageNumberPagination

from .models import Sensor, Event
from .service import EventFilter, readJsonEvents
from .serializers import SensorSerializer, EventSerializer
from sensors_api.settings import UPLOAD_FILE

from json import JSONDecodeError


@api_view(['GET'])
def apiOverview(request):
    api_sensor_urls = {
        'List sensor: /sensor-list/',
        'Create sensor: /sensor-detail/<str:pk>',
        'Update sensor: /sensor-update/<str:pk>',
        'Delete sensor: /sensor-delete/<str:pk>',
        'Get sensor events: /sensor-events/<str:pk>',
    }
    api_event_urls = {
        'List event: /event-list/',
        'Create event: /event-detail/<str:pk>',
        'Update event: /event-update/<str:pk>',
        'Delete event: /event-delete/<str:pk>',
        'Filter event: /event-list/?humidity_min=*&&temperature_value=*&&...etc',
        'Upload *.json events: /event-upload/',
    }
    return Response([api_sensor_urls, api_event_urls])


# _____________ SENSOR _______________
@api_view(['GET'])
def sensorList(request):
    sensors = Sensor.objects.all()
    serializer = SensorSerializer(sensors, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def sensorDetail(request, pk):
    try:
        sensor = Sensor.objects.get(id=pk)
    except Sensor.DoesNotExist:
        raise NotFound('Sensor not found')
    serializer = SensorSerializer(sensor, many=False)
    return Response(serializer.data)


@api_view(['POST', 'GET'])
def sensorCreate(request):
    serializer = SensorSerializer(data=request.data)
    if request.method == 'GET':
        return Response('Create a sensor')
    if request.method == 'POST':
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'PATCH', 'GET'])
def sensorUpdate(request, pk):
    try:
        sensor = Sensor.objects.get(id=pk)
    except Sensor.DoesNotExist:
        raise NotFound('Sensor not found')
    serializer = SensorSerializer(instance=sensor,
                                  data=request.data)
    if request.method == 'GET':
        serializer = SensorSerializer(sensor, many=False)
        return Response(serializer.data)
    elif request.method == 'PUT':
        serializer = SensorSerializer(instance=sensor, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        serializer = SensorSerializer(instance=sensor,
                                      data=request.data,
                                      partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE', 'GET'])
def sensorDelete(request, pk):
    try: 
        sensor = Sensor.objects.get(id=pk)
    except Sensor.DoesNotExist:
        raise NotFound('Sensor not found')
    if request.method == 'GET':
        sensor = Sensor.objects.get(id=pk)
        serializer = SensorSerializer(sensor,
                                      many=False)
        return Response(serializer.data)
    elif request.method == 'DELETE':
        sensor = Sensor.objects.get(id=pk)
        sensor.delete()
        return Response('Successfuly deleted!',
                        status=status.HTTP_204_NO_CONTENT)


# ___________EVENT______________
@api_view(['GET'])
def eventList(request):
    events = Event.objects.all()

    # pagination pages
    paginator = PageNumberPagination()
    paginator.page_size = 5

    # filter by temp, hum param
    filterset_class = EventFilter
    filtered_events = filterset_class(request.GET, queryset=events).qs

    result = paginator.paginate_queryset(filtered_events, request)
    serializer = EventSerializer(result, many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view(['GET'])
def eventDetail(request, pk):
    try:
        event = Event.objects.get(id=pk)
    except Event.DoesNotExist:
        raise NotFound('Event not found')
    serializer = EventSerializer(event, many=False)
    return Response(serializer.data)


@api_view(['POST', 'GET'])
def eventCreate(request):
    serializer = EventSerializer(data=request.data)
    if request.method == 'GET':
        return Response('Create an event')
    if request.method == 'POST':
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'PATCH', 'GET'])
def eventUpdate(request, pk):
    try:
        event = Event.objects.get(id=pk)
    except Event.DoesNotExist:
        raise NotFound('Event not found')
    serializer = EventSerializer(instance=event,
                                 data=request.data)
    if request.method == 'GET':
        event = Event.objects.get(id=pk)
        serializer = EventSerializer(event, many=False)
        return Response(serializer.data)
    elif request.method == 'PUT':
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'PATCH':
        serializer = EventSerializer(instance=event,
                                     data=request.data,
                                     partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data,
                            status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors,
                            status=status.HTTP_400_BAD_REQUEST)


@api_view(['DELETE', 'GET'])
def eventDelete(request, pk):
    try:
        event = Event.objects.get(id=pk)
    except Event.DoesNotExist:
        raise NotFound('Event not found')
    if request.method == 'GET':
        serializer = EventSerializer(event, many=False)
        return Response(serializer.data)
    if request.method == 'DELETE':
        event = Event.objects.get(id=pk)
        event.delete()
        return Response('Successfuly deleted!',
                        status=status.HTTP_204_NO_CONTENT)


@api_view(['GET'])
def getEventListFromSensor(request, pk):
    try:
        events = Event.objects.filter(sensor_id=pk)
    except Sensor.DoesNotExist:
        raise NotFound('Sensor not found')
    serializer = EventSerializer(events, many=True)
    return Response(serializer.data)


@api_view(['POST', 'GET'])
def uploadJsonEvents(request):
    try:
        data = readJsonEvents()
        data_success = []
        data_fail = []
        if request.method == 'GET':
            return Response(f'Upload {UPLOAD_FILE}')
        for frame in data:
            serializer = EventSerializer(data=[frame], many=True)
            if request.method == 'POST':
                if serializer.is_valid():
                    serializer.save()
                    data_success += [frame]
                else:
                    data_fail += [frame]
            else:
                return Response(serializer.errors, 
                                status=status.HTTP_400_BAD_REQUEST)
        return Response(f'Success: {data_success}\
                          Failed: {data_fail},\
                          ERROR: {serializer.errors}')
    except (JSONDecodeError, FileNotFoundError):
        return Response('Json file is damaged or not found', 
                        status=status.HTTP_400_BAD_REQUEST)