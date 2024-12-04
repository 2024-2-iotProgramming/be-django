from django.contrib import admin

from . import models


@admin.register(models.RadarSensor)
class ModelAdmin(admin.ModelAdmin):
    list_display = ('is_occupied', 'model', 'echo_cm', 'timestamp')
    search_fields = ('x', 'y')
    list_per_page = 100
    list_max_show_all = 1000


@admin.register(models.Seat)
class ModelAdmin(admin.ModelAdmin):
    list_display = ('x', 'y', 'is_occupied')
    list_filter =  ('x', 'y')
    search_fields = ('x', 'y')
    list_per_page = 100
    list_max_show_all = 1000
