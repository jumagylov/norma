from django.contrib import admin

from .models import Equipments


class EquipmentsModelsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Equipments._meta.fields]

    class Meta:
        model = Equipments


admin.site.register(Equipments, EquipmentsModelsAdmin)
