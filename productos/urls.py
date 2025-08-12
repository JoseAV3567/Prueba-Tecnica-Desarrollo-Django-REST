

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


urlpatterns = form_urls + router.urls
