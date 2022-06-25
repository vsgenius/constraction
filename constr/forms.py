from django.forms import ModelForm

from constr.models import Flights


class FlightsForm(ModelForm):
    class Meta:
        model = Flights
        fields = '__all__'