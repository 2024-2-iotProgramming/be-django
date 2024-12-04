from django.contrib import admin
from django.db import models


class SeatXChoices(models.IntegerChoices):
    X0 = 0
    X1 = 1


class Seat(models.Model):
    x = models.IntegerField(choices=SeatXChoices.choices)
    y = models.IntegerField()
    occupied = models.BooleanField()

    class Meta:
        unique_together = ('x', 'y')

    def __str__(self) -> str:
        return f'(x={self.x}, y={self.y})'


class RadarSensor(models.Model):
    x = models.IntegerField(choices=SeatXChoices.choices)
    y = models.IntegerField()
    model = models.CharField(default='HC-SR04', max_length=20)
    echo_cm = models.FloatField()
    timestamp = models.DateTimeField(auto_now_add=True)

    @admin.display(boolean=True)
    def occupied(self) -> bool:
        return self.echo_cm < 90.0

    @admin.display()
    def seat(self) -> Seat:
        return Seat.objects.get_or_create(x=self.x, y=self.y)[0]

    def save(self, *args, **kwargs) -> None:
        super().save(*args, **kwargs)
        obj: Seat = self.seat()
        obj.occupied = self.occupied()
        obj.save()
