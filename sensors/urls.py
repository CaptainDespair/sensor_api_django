from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    path('sensor-list/', views.sensorList, name='sensor-list'),
    path('sensor-detail/<str:pk>', views.sensorDetail, name='sensor-detail'),
    path('sensor-create/', views.sensorCreate, name='sensor-create'),
    path('sensor-update/<str:pk>', views.sensorUpdate, name='sensor-update'),
    path('sensor-delete/<str:pk>', views.sensorDelete, name='sensor-delete'),
    path('event-list/', views.eventList, name='event-list'),
    path('event-detail/<str:pk>', views.eventDetail, name='event-detail'),
    path('event-create/', views.eventCreate, name='event-create'),
    path('event-update/<str:pk>', views.eventUpdate, name='event-update'),
    path('event-delete/<str:pk>', views.eventDelete, name='event-delete'),
    path('sensor-events/<str:pk>', views.getEventListFromSensor, name='sensor-events'),
    path('event-upload/', views.uploadJsonEvents, name='event-upload')
]
