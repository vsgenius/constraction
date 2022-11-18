from django.urls import path
from constr.views import index, flight, add_and_save, trucks, careers, warehouses, validate_geo

urlpatterns = [
    path('',index, name='index'),
    path('flight/<int:flights_id>/', flight, name='flight'),
    path('flight/add/', add_and_save, name='add'),
    path('careers/', careers, name='careers'),
    path('trucks/', trucks, name='trucks'),
    path('warehouses/', warehouses, name='warehouses'),
]
