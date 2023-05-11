from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework.pagination import PageNumberPagination

from .serializers import SensorSerializer, EventSerializer
from .models import Sensor, Event


@api_view(['GET'])
def apiOverview(request):
    api_sensor_urls = {
        'List sensor: /sensor-list/',
        'Create sensor: /sensor-detail/<str:pk>',
        'Update sensor: /sensor-update/<str:pk>',
        'Delete sensor: /sensor-delete/<str:pk>',
    }
    api_event_urls = {
        'List event: /event-list/',
        'Create event: /event-detail/<str:pk>',
        'Update event: /event-update/<str:pk>',
        'Delete event: /event-delete/<str:pk>',
    }
    return Response([api_sensor_urls, api_event_urls])

# _____________ SENSOR CRUD ________________

@api_view(['GET'])
def sensorList(request):
    sensors = Sensor.objects.all()
    serializer = SensorSerializer(sensors, many=True)
    return Response(serializer.data)


@api_view(['GET'])
def sensorDetail(request, pk):
    sensor = Sensor.objects.get(id=pk)
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
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'PATCH', 'GET'])
def sensorUpdate(request, pk):
    sensor = Sensor.objects.get(id=pk)
    serializer = SensorSerializer(instance=sensor, data=request.data)
    if request.method == 'GET':
        sensor = Sensor.objects.get(id=pk)
        serializer = SensorSerializer(sensor, many=False)
        return Response(serializer.data)
    if request.method == 'PUT':
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'PATCH':
        serializer = SensorSerializer(instance=sensor, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    
    

@api_view(['DELETE', 'GET'])
def sensorDelete(request, pk):
    if request.method == 'GET':
        sensor = Sensor.objects.get(id=pk)
        serializer = SensorSerializer(sensor, many=False)
        return Response(serializer.data)
    if request.method == 'DELETE':
        sensor = Sensor.objects.get(id=pk)
        sensor.delete()
        return Response('Successfuly deleted!')


# ___________EVENT CRUD ______________

@api_view(['GET'])
def eventList(request):
    paginator = PageNumberPagination()
    paginator.page_size = 5
    events = Event.objects.all()
    result = paginator.paginate_queryset(events, request)
    serializer = EventSerializer(result, many=True)
    return paginator.get_paginated_response(serializer.data)


@api_view(['GET'])
def eventDetail(request, pk):
    event = Event.objects.get(id=pk)
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
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['PUT', 'PATCH', 'GET'])
def eventUpdate(request, pk):
    event = Event.objects.get(id=pk)
    serializer = EventSerializer(instance=event, data=request.data)
    if request.method == 'GET':
        event = Event.objects.get(id=pk)
        serializer = EventSerializer(event, many=False)
        return Response(serializer.data)
    if request.method == 'PUT':
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'PATCH':
        serializer = EventSerializer(instance=event, data=request.data, partial=True)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)    


@api_view(['DELETE', 'GET'])
def eventDelete(request, pk):
    if request.method == 'GET':
        event = Event.objects.get(id=pk)
        serializer = EventSerializer(event, many=False)
        return Response(serializer.data)
    if request.method == 'DELETE':
        event = Event.objects.get(id=pk)
        event.delete()
        return Response('Successfuly deleted!')
    

@api_view(['GET'])
def getEventListFromSensor(request, pk):
    events = Event.objects.filter(sensor_id=pk)
    serializer = EventSerializer(events, many=True)
    return Response(serializer.data)


# class SensorListView(ListView):
#     model = Sensor
# class SensorCreateView(CreateView):
#     model = Sensor
#     fields = ['name', 'type']
# class SensorDeleteView(DeleteView):
#     model = Sensor
#     success_url = reverse_lazy('sensors:sensors_all')
# class SensorUpdateView(UpdateView):
#     model = Sensor
#     fields = ['name', 'type']
# class EventListView(ListView):
#     model = Event
# class EventCreateView(CreateView):
#     model = Event
#     fields = ['sensor_id', 'name', 'temperature', 'humidity']
# class EventDeleteView(DeleteView):
#     model = Event
#     success_url = reverse_lazy('sensors:events_all')
# class EventUpdateView(UpdateView):
#     model = Event
#     fields = ['sensor_id', 'name', 'temperature', 'humidity']
