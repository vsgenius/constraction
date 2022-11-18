
from django.contrib import admin
from django.urls import path, include
from rest_framework import routers

from api.api import TrucksViewSet, FlightsViewSet, СareersViewSet, WarehousesViewSet
from constr.views import validate_geo

router = routers.DefaultRouter()
router.register('flight',FlightsViewSet,'product')
router.register('careers',СareersViewSet,'shop')
router.register('trucks',TrucksViewSet,'basket')
router.register('warehouses',WarehousesViewSet,'orders')
urlpatterns = [
    path('',include(router.urls)),
    path('validate_geo/', validate_geo, name='validate_geo')
]