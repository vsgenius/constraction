from geographiclib.geodesic import Geodesic
from rest_framework.permissions import BasePermission

from constr.models import Warehouses


def validate_geo(request):
        coordinates = request.POST.get('coordinates',None)
        warehouse_id = request.POST.get('warehouse_id', None)
        warehouse = Warehouses.objects.filter(id=warehouse_id)[0].coordinates.split(',')
        coordinates = coordinates.split(',')
        geod = Geodesic.WGS84
        g = geod.Inverse(float(coordinates[0]), float(coordinates[1]), float(warehouse[0]), float(warehouse[1]))
        # print("{:.2f}".format(g['s12']))
        if g['s12'] < 5:
            return True
        return False