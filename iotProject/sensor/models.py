from django.db import models


class RadarSensorDirection(models.TextChoices):
	Y_POS = '+y'
	Y_NEG = '-y'


class RadarSensor(models.Model):
	model = models.CharField(default='HC-SR04', max_length=20)
	direction = models.TimeField(choices=RadarSensorDirection.choices)
	echo_cm = models.FloatField()
	created_at = models.DateTimeField()
