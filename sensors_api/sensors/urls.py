from django.urls import path
from . import views

urlpatterns = [
    path('', views.apiOverview, name='api-overview'),
    path('sensor-list/', views.sensorList, name='sensor-list'),
    path('sensor-detail/<str:pk>', views.sensorDetail, name='sensor-detail'),
    path('sensor-create/', views.sensorCreate, name='sensor-create'),
    path('sensor-update/<str:pk>', views.sensorUpdate, name='sensor-update'),
    path('sensor-delete/<str:pk>', views.sensorDelete, name='sensor-delete'),
]
