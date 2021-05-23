from rest_framework import serializers
from .models import Equipments


class EquipmentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Equipments
        fields = ['description', 'title', 'image']
