from django.contrib import admin

from .models import Equipments, Ofd


class EquipmentsModelsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Equipments._meta.fields]

    class Meta:
        model = Equipments


admin.site.register(Equipments, EquipmentsModelsAdmin)


class OfdModelsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in Ofd._meta.fields]

    class Meta:
        model = Ofd


admin.site.register(Ofd, OfdModelsAdmin)
