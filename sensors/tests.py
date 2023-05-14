from django.urls import reverse
from rest_framework import status
from rest_framework.test import APITestCase
from sensors.models import Sensor


class SensorTests(APITestCase):

    def setUp(self):
        self.sensor = Sensor.objects.create(name='Sensor1', type='1')
        self.sensor_is_valid = {'name': 'SensorX', 'type': 1}
        self.sensor_is_invalid = {'name': '', 'type': 4}

    def test_sensorList(self):
        url = reverse('sensor-list')
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(len(response.data), 1)
        self.assertEqual(response.data[0]['name'], 'Sensor1')

    def test_sensorDetail(self):
        url = reverse('sensor-detail', args=[self.sensor.id])
        response = self.client.get(url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response.data['name'], 'Sensor1')

    def test_sensorValidCreate(self):
        url = reverse('sensor-create')
        response = self.client.post(url, self.sensor_is_valid, fromat='json')
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
        self.assertEqual(Sensor.objects.count(), 2)

    def test_sensorInvalidCreate(self):
        url = reverse('sensor-create')
        response = self.client.post(url, self.sensor_is_invalid, fromat='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_sensorUpdate(self):
        url = reverse('sensor-update', args=[self.sensor.id])
        updated_sensor = {'name': 'Sensor2', 'type': 2}
        response = self.client.patch(url, updated_sensor, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.sensor.refresh_from_db()
        self.assertEqual(self.sensor.name, 'Sensor2')

    def test_sensorDelete(self):
        url = reverse('sensor-delete', args=[self.sensor.id])
        response = self.client.delete(url)
        self.assertEqual(response.status_code, status.HTTP_204_NO_CONTENT)
        self.assertEqual(Sensor.objects.count(), 0)
