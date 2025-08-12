

from django.urls import path


from .views import (
    ProductoListView,
    ProductoDetailView,
    ProductoCreateView,
    ProductoUpdateView,
    ProductoDeleteView,
)

from rest_framework.routers import DefaultRouter
from productos.ControladorProductos import ProductosApiView


router = DefaultRouter()

router.register(r"inventario", ProductosApiView, basename="producto-api")

urlpatterns =  router.urls
