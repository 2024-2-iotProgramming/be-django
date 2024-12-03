from django.db import models


class RadarSensorDirection(models.TextChoices):
	Y_POS = '+y'
	Y_NEG = '-y'


class RadarSensor(models.Model):
	model = models.CharField(default='HC-SR04', max_length=20)
	position = models.IntegerField()
	direction = models.TimeField(choices=RadarSensorDirection.choices)
	echo_cm = models.FloatField()
	timestamp = models.DateTimeField()


class Seat(models.Model):
	seat_number = models.IntegerField()
	occupied = models.BooleanField(default=False)
