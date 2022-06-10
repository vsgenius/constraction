from django.contrib import admin

from constr.models import Сareers, Trucks, Warehouses, Flights


@admin.register(Сareers)
class СareersAdmin(admin.ModelAdmin):
    list_display = ('title', 'description', 'coordinates', 'date')


@admin.register(Trucks)
class TrucksAdmin(admin.ModelAdmin):
    list_display = ('brand', 'model', 'number', 'capacity','date')


@admin.register(Warehouses)
class WarehousesAdmin(admin.ModelAdmin):
    list_display = ('title', 'coordinates', 'date')


@admin.register(Flights)
class FlightsAdmin(admin.ModelAdmin):
    list_display = ('date_Flight', 'truck_id', 'career_id','warehouse_id','weight','coordinates','completed','date')