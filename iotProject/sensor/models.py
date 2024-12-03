from django.db import models


class RadarSensor(models.Model):
    x = models.IntegerField(choices=[(0, 0), (1, 1)])
    y = models.IntegerField()
    model = models.CharField(default='HC-SR04', max_length=20)
    echo_cm = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)


class Seat(models.Model):
    x = models.IntegerField()
    y = models.IntegerField()
    occupied = models.BooleanField(default=False)

    class Meta:
        unique_together = ('x', 'y')
