from rest_framework import serializers

from . import models


class RadarSensorSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.RadarSensor
        fields = '__all__'


class SeatSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Seat
        fields = '__all__'
