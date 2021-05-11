from rest_framework import serializers
from .models import OrderModels, ClientModels


class OrderModelsSerializer(serializers.ModelSerializer):

    class Meta:
        model = OrderModels
        fields = '__all__'


class ClientModelsSerializer(serializers.ModelSerializer):

    class Meta:
        model = ClientModels
        fields = '__all__'
