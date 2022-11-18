from rest_framework import viewsets, permissions, status
from rest_framework.response import Response

from api.serialisers import СareersSerializers, TrucksSerializers, WarehousesSerializers, \
    FlightsSerializers
from constr.models import Сareers, Trucks, Warehouses, Flights
from constr.permissions import validate_geo


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

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        if validate_geo(request):
            self.perform_create(serializer)
            headers = self.get_success_headers(serializer.data)
            return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
        return Response(data={'error':'Координаты не соответствуют складу'}, status=status.HTTP_400_BAD_REQUEST)