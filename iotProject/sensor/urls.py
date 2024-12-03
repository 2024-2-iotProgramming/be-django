from django.urls import path

from . import views

urlpatterns = [
    path('sensor/radar/', views.RadarSensorListCreate.as_view()),
    path('seat/', views.SeatList.as_view()),
]
