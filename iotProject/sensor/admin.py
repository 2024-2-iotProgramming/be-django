from django.contrib import admin

from . import models


@admin.register(models.RadarSensor)
class ModelAdmin(admin.ModelAdmin):
    list_display = ('seat', 'occupied', 'model', 'echo_cm', 'timestamp')
    search_fields = ('x', 'y')
    list_per_page = 100
    list_max_show_all = 1000


@admin.register(models.Seat)
class ModelAdmin(admin.ModelAdmin):
    list_display = ('x', 'y', 'occupied')
    list_filter = ('occupied',)
    search_fields = ('x', 'y')
    list_per_page = 100
    list_max_show_all = 1000
