from rest_framework import viewsets, permissions

from api.serialisers import СareersSerializers, TrucksSerializers, WarehousesSerializers, \
    FlightsSerializers
from constr.models import Сareers, Trucks, Warehouses, Flights


class СareersViewSet(viewsets.ModelViewSet):
    queryset = Сareers.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = СareersSerializers


class TrucksViewSet(viewsets.ModelViewSet):
    queryset = Trucks.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = TrucksSerializers


class WarehousesViewSet(viewsets.ModelViewSet):
    queryset = Warehouses.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = WarehousesSerializers


class FlightsViewSet(viewsets.ModelViewSet):
    queryset = Flights.objects.all()
    permission_classes = [
        permissions.AllowAny
    ]
    serializer_class = FlightsSerializers
