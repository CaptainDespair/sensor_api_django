from django.shortcuts import render
from django.urls import reverse_lazy
from django.http import response

from django.views.generic import ListView
from django.views.generic.edit import CreateView, DeleteView, UpdateView

from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status

from .serializers import SensorSerializer
from .models import Sensor, Event


@api_view(['GET'])
def apiOverview(request):
    api_urls = {
        'List: /sensor-list/',
        'Create: /sensor-detail/<str:pk>',
        'Update: /sensor-update/<str:pk>',
        'Delete: /sensor-delete/<str:pk>',
    }
    return Response(api_urls)


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


@api_view(['PUT', 'GET'])
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
