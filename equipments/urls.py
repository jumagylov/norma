from django.urls import include, path
from rest_framework import routers

from .views import EquipmentsViewSet, OfdViewSet

app_name = 'Equipments'

router = routers.DefaultRouter()
router.register('equipments', EquipmentsViewSet, basename='equipments'),
router.register('Ofd', OfdViewSet, basename='ofd'),

urlpatterns = [
    path('', include(router.urls)),
]
