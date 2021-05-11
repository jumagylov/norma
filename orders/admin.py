from django.contrib import admin
from .models import OrderModels, ClientModels


class OrderModelsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in OrderModels._meta.fields]

    class Meta:
        model = OrderModels


admin.site.register(OrderModels, OrderModelsAdmin)


class ClientModelsAdmin(admin.ModelAdmin):
    list_display = [field.name for field in ClientModels._meta.fields]

    class Meta:
        model = ClientModels


admin.site.register(ClientModels, ClientModelsAdmin)

