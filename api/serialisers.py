from rest_framework import serializers

from constr.models import Сareers, Trucks, Warehouses, Flights


class СareersSerializers(serializers.ModelSerializer):
    class Meta:
        model = Сareers
        fields = '__all__'


class TrucksSerializers(serializers.ModelSerializer):

    class Meta:
        model = Trucks
        fields = '__all__'


class WarehousesSerializers(serializers.ModelSerializer):
    class Meta:
        model = Warehouses
        fields = '__all__'


class FlightsSerializers(serializers.ModelSerializer):


    class Meta:
        model = Flights
        fields = '__all__'


