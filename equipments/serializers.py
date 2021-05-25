from rest_framework import serializers
from .models import Equipments, Ofd


class EquipmentsSerializer(serializers.ModelSerializer):

    class Meta:
        model = Equipments
        fields = '__all__'


class OfdSerializer(serializers.ModelSerializer):
    class Meta:
        model = Ofd
        fields = '__all__'
