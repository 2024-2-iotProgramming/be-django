from rest_framework import generics
from rest_framework import serializers
from rest_framework import throttling

from . import models


class RadarSensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RadarSensor
        exclude = ('id',)


class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Seat
        exclude = ('id',)


class RadorSensorCreateThrottle(throttling.SimpleRateThrottle):
    scope = 'radar_sensor_create'
    rate = '20/sec'

    def get_cache_key(self, request, view):
        return True


class RadarSensorListCreate(generics.ListCreateAPIView):
    queryset = models.RadarSensor.objects.all()
    serializer_class = RadarSensorSerializer
    throttle_classes = [RadorSensorCreateThrottle]


class SeatList(generics.ListAPIView):
    queryset = models.Seat.objects.all()
    serializer_class = SeatSerializer
