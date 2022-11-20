from django.urls import path, include
from rest_framework import routers

from api.api import TrucksViewSet, FlightsViewSet, СareersViewSet, WarehousesViewSet

router = routers.DefaultRouter()
router.register('flight',FlightsViewSet,'product')
router.register('careers',СareersViewSet,'shop')
router.register('trucks',TrucksViewSet,'basket')
router.register('warehouses',WarehousesViewSet,'orders')
urlpatterns = [
    path('',include(router.urls))
]