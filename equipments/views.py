from django.core.mail import send_mail
from rest_framework import viewsets
from rest_framework.response import Response
from rest_framework import status
from .models import Ofd
from unnamed_project.settings import EMAIL_HOST_USER
from .models import Equipments
from .serializers import EquipmentsSerializer, OfdSerializer
# nnormalkg@gmail.com


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


class OfdViewSet(viewsets.ModelViewSet):
    serializer_class = OfdSerializer
    queryset = Ofd.objects.all()
    http_method_names = ['post']

    def get(self):
        image = self.queryset.all()
        serializer = self.serializer_class(image, many=True)
        return Response(serializer.data, status=status.HTTP_200_OK)



    def create(self, request, *args, **kwargs):
        data = request.data
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_create(serializer)
        headers = self.get_success_headers(serializer.data)
        send_mail('Новый заказ', f'Пользователь {data["first_name"]} заказал {data["product"]}.\n'
                  f'Его данные: номер телефона-{data["phone"]}, адрес-{data["address"]}, email -{"email"}.\n'
                  f'фото-{data["images"]}',
                  EMAIL_HOST_USER, ['jumagylov655@gmail.com'])
        return Response(serializer.data, status=status.HTTP_201_CREATED, headers=headers)
