# productos/urls.py

from django.urls import path

# Asegúrate de importar todas las vistas que necesitas
from .views import (
    ProductoListView,
    ProductoDetailView,
    ProductoCreateView,
    ProductoUpdateView,
    ProductoDeleteView,
)

from rest_framework.routers import DefaultRouter
from productos.ControladorProductos import ProductosApiView

# 1. Definimos el router para la API (lo que ve Swagger)
router = DefaultRouter()
# Es buena práctica usar un 'basename' único para la API para evitar conflictos
router.register(r"inventario", ProductosApiView, basename="producto-api")

# 2. Definimos la lista de URLs para el CRUD con formularios
form_urls = [
    path("", ProductoListView.as_view(), name="lista-productos"),
    path("producto/<int:pk>/", ProductoDetailView.as_view(), name="detalle-producto"),
    path("producto/nuevo/", ProductoCreateView.as_view(), name="crear-producto"),
    path(
        "producto/<int:pk>/editar/",
        ProductoUpdateView.as_view(),
        name="actualizar-producto",
    ),
    path(
        "producto/<int:pk>/borrar/",
        ProductoDeleteView.as_view(),
        name="borrar-producto",
    ),
]

# 3. Combinamos AMBAS listas en urlpatterns
# El truco es simplemente sumarlas
urlpatterns = form_urls + router.urls
