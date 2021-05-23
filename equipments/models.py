from django.db import models


class Equipments(models.Model):
    description = models.TextField(max_length=100)
    title = models.CharField(max_length=100)
    image = models.ImageField(upload_to='equipments/images')

    def __str__(self):
        return self.description
