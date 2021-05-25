from django.db import models


class Equipments(models.Model):
    description = models.TextField(max_length=100)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='equipments/images')

    def __str__(self):
        return self.description


class Ofd(models.Model):

    first_name = models.CharField(max_length=24)
    company = models.CharField(max_length=24)
    phone = models.CharField(max_length=24)
    address = models.CharField(max_length=64)
    product = models.CharField(max_length=64)
    email = models.CharField(max_length=30)
    images = models.ImageField(upload_to='ofd/images')

    def __str__(self):
        return f'{self.first_name}, {self.company}'

    class Meta:
        verbose_name = 'заказ'
        verbose_name_plural = 'заказы'
