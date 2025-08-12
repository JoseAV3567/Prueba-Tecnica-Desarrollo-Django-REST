from rest_framework.viewsets import ModelViewSet  # <- CAMBIAR AQUÍ
from rest_framework.response import Response
from rest_framework import status

from .models import Productos
from .serializers import ProductosSerializers



class ProductosApiView(ModelViewSet):
    serializer_class = ProductosSerializers
    queryset = Productos.objects.all().order_by("-pk")

    def create(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
       
            headers = self.get_success_headers(serializer.data)
            return Response(
                serializer.data, status=status.HTTP_201_CREATED, headers=headers
            )

        return Response(
            {"error": "Error al crear el producto", "detalles": serializer.errors},
            status=status.HTTP_400_BAD_REQUEST,
        )

    def update(self, request, *args, **kwargs):
        instance = self.get_object()
        serializer = self.get_serializer(instance, data=request.data)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response({"message": "Producto actualizado correctamente"})

    def destroy(self, request, *args, **kwargs):
        instance = self.get_object()
        self.perform_destroy(instance)
        return Response(
            {"message": "Producto eliminado correctamente"},
            status=status.HTTP_204_NO_CONTENT,
        )
