from django.urls import include, path
from rest_framework import routers

from .views import EquipmentsViewSet

app_name = 'Equipments'

router = routers.DefaultRouter()
router.register('equipments', EquipmentsViewSet, basename='equipments')

urlpatterns = [
    path('', include(router.urls)),
]
