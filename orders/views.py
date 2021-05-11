from django.shortcuts import render
from django.core.mail import send_mail

from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status

from .models import OrderModels, ClientModels
from .serializer import OrderModelsSerializer, ClientModelsSerializer
from unnamed_project.settings import EMAIL_HOST_USER


class OrderSafeAndSendEmailViewSet(viewsets.ModelViewSet):
    serializer_class = OrderModelsSerializer
    queryset = OrderModels
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        send_mail('Новый заказ', f'Пользователь {data["first_name"]} заказал {data["product"]}.\n'
                  f'Его данные: номер телефона-{data["phone"]}, адрес-{data["address"]}',
                  EMAIL_HOST_USER, ['djanbolotov03@gmail.com'])
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)


class OrderSafeAndSendClientViewSet(viewsets.ModelViewSet):

    serializer_class = ClientModelsSerializer
    queryset = ClientModels
    http_method_names = ['post']

    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        send_mail('отправить', f'номер телефона {data["phone_number"]}',
                  EMAIL_HOST_USER, ['nnormalkg@gmail.com'])
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)

