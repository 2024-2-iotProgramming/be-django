from django.contrib import admin
from django.db import models


class SeatXChoices(models.IntegerChoices):
    X0 = 0
    X1 = 1


SEAT_RADAR_MULTIPLIER = 28  # 20번 측정 = 1석
RADAR_ECHO_OCCUPIED_THRESHOLD = 90.0  # cm


class Seat(models.Model):
    x = models.IntegerField(choices=SeatXChoices.choices)
    y = models.IntegerField()

    class Meta:
        unique_together = ('x', 'y')

    def __str__(self) -> str:
        return f'(x={self.x}, y={self.y})'

    @admin.display(boolean=True)
    def is_occupied(self) -> bool:
        # TODO: 당장 이 방식은 시간복잡도가 박살났지만, 좌석 수가 적으니 일단 강행하자.
        sy = SEAT_RADAR_MULTIPLIER*self.y
        ey = SEAT_RADAR_MULTIPLIER*(self.y+1)
        for y in range(sy, ey):
            queryset = RadarSensor.objects.filter(x=self.x, y=y)
            if queryset.exists() and queryset.latest().is_occupied:
                return True
        return False


class RadarSensor(models.Model):
    x = models.IntegerField(choices=SeatXChoices.choices)
    y = models.IntegerField()
    model = models.CharField(default='HC-SR04', max_length=20)
    echo_cm = models.FloatField()
    is_occupied = models.BooleanField(default=False)
    timestamp = models.DateTimeField(auto_now_add=True)

    def save(self, *args, **kwargs) -> None:
        self.is_occupied = self.echo_cm < RADAR_ECHO_OCCUPIED_THRESHOLD
        super().save(*args, **kwargs)
        self.ensure_corresponding_seat()

    def ensure_corresponding_seat(self) -> None:
        seats_kwargs = {
            'x': self.x,
            'y': self.y//SEAT_RADAR_MULTIPLIER,
        }
        if not Seat.objects.filter(**seats_kwargs).exists():
            Seat.objects.create(**seats_kwargs)

    class Meta:
        get_latest_by = ('-timestamp',)
