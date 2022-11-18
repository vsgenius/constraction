from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.shortcuts import render
from django.urls import reverse_lazy, reverse
from django.views.generic import CreateView
from geographiclib.geodesic import Geodesic
from constr.forms import FlightsForm
from constr.models import Flights, Trucks, Warehouses, Сareers


def index(request):
    flights = Flights.objects.all()
    context = {'flights': flights}
    return render(request, 'index.html', context)


def trucks(request):
    truck = Trucks.objects.all()
    context = {'trucks': truck}
    return render(request, 'trucks.html', context)


def warehouses(request):
    warehouse = Warehouses.objects.all()
    context = {'warehouses': warehouse}
    return render(request, 'warehouses.html', context)


def careers(request):
    career = Сareers.objects.all()
    context = {'careers': career}
    return render(request, 'careers.html', context)


# def constr(request):
#     flights = Flights.objects.all()
#     context = {'flights':flights}
#     return render(request, 'constr.html', context)


def flight(request, flights_id):
    flights = Flights.objects.all()
    current_flight = Flights.objects.get(pk=flights_id)
    context = {'flights': flights, 'current_flight': current_flight}
    return render(request, 'by_flights.html', context)


def add_and_save(request):
    if request.method == 'POST':
        flf = FlightsForm(request.POST)
        flf.save()
        return HttpResponseRedirect(reverse('index'))
    else:
        flf = FlightsForm()
        context = {'form': flf}
        return render(request, 'create.html', context)


def validate_geo(request):
        coordinates = request.GET.get('coordinates',None)
        warehouse_id = request.GET.get('warehouse_id', None)
        warehouse = Warehouses.objects.filter(id=warehouse_id)[0].coordinates.split(',')
        coordinates = coordinates.split(',')
        geod = Geodesic.WGS84
        g = geod.Inverse(float(coordinates[0]), float(coordinates[1]), float(warehouse[0]), float(warehouse[1]))
        # print("{:.2f}".format(g['s12']))
        if g['s12'] < 5:
            response = {
                'is_taken': True
            }
        else:
            response = {
                'is_taken': False
            }
        return response.is_taken