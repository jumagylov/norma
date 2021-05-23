from django.shortcuts import render
from rest_framework import viewsets
from django.http import Http404
from rest_framework import viewsets, status
from rest_framework.response import Response
from rest_framework.exceptions import ParseError

from .models import Equipments
from .serializers import EquipmentsSerializer


class EquipmentsViewSet(viewsets.ModelViewSet):
    serializer_class = EquipmentsSerializer
    queryset = Equipments.objects.all()
    http_method_names = ['post']

    def get(self):
        image = self.queryset.all()
        serializer = self.serializer_class(image, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def create(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data, context={'request': request})
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)
