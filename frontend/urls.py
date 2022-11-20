from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('',TemplateView.as_view(template_name='main.html'),
         name='main')
    # path('flight/<int:flights_id>/', flight, name='flight'),
    # path('flight/add/', add_and_save, name='add'),
    # path('careers/', careers, name='careers'),
    # path('trucks/', trucks, name='trucks'),
    # path('warehouses/', warehouses, name='warehouses'),
]