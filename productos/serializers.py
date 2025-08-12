from rest_framework.serializers import ModelSerializer
from datetime import datetime
from productos.models import *


class ProductosSerializers(ModelSerializer):
    def to_representation(self, instance: Productos):
        return {
            "id": instance.pk,
            "nombre": f"{instance.nombre}",
            "descripcion": f"{instance.descripcion}",
            "precio": f"{instance.precio}",
            "disponible": f"{instance.disponible}",
        }

    class Meta:
        model = Productos
        fields = "__all__"
