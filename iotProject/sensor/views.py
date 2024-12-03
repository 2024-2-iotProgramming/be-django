from rest_framework import generics

from . import models
from . import serializers


class RadarSensorListCreate(generics.ListCreateAPIView):
    queryset = models.RadarSensor
    serializer_class = serializers.RadarSensorSerializer


class SeatList(generics.ListAPIView):
    queryset = models.Seat
    serializer_class = serializers.SeatSerializer
