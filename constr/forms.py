from django.forms import ModelForm

from constr.models import Flights


class FlightsForm(ModelForm):
    class Meta:
        model = Flights
        fields = {'date_Flight', 'truck_id', 'career_id', 'warehouse_id', 'weight', 'coordinates', 'completed'}