# productos/views.py
from django.urls import reverse_lazy
from django.views.generic import (
    ListView,
    DetailView,
    CreateView,
    UpdateView,
    DeleteView,
)
from .models import Productos
from .forms import ProductoForm


# Vista para LEER (Listar todos los productos)
class ProductoListView(ListView):
    model = Productos
    template_name = "productos/templates/lista_productos.html"  # Plantilla a usar
    context_object_name = "productos"  # Nombre para la lista en la plantilla


# Vista para LEER (Ver el detalle de un solo producto)
class ProductoDetailView(DetailView):
    model = Productos
    template_name = "productos/templates/detalle_producto.html"
    context_object_name = "producto"


# Vista para CREAR un nuevo producto
class ProductoCreateView(CreateView):
    model = Productos
    form_class = ProductoForm  # Usa nuestro formulario personalizado
    template_name = "productos/templates/formulario_producto.html"
    # URL a la que se redirige si la creación es exitosa
    # Usamos reverse_lazy para que la URL se evalúe cuando sea necesario
    success_url = reverse_lazy("lista-productos")


# Vista para ACTUALIZAR un producto existente
class ProductoUpdateView(UpdateView):
    model = Productos
    form_class = ProductoForm
    template_name = "productos/templates/formulario_producto.html"
    success_url = reverse_lazy("lista-productos")


# Vista para BORRAR un producto
class ProductoDeleteView(DeleteView):
    model = Productos
    template_name = "productos/templates/confirmar_borrado.html"
    success_url = reverse_lazy("lista-productos")
