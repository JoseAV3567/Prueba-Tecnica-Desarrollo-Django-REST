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



class ProductoListView(ListView):
    model = Productos
    template_name = "productos/templates/lista_productos.html" 
    context_object_name = "productos" 



class ProductoDetailView(DetailView):
    model = Productos
    template_name = "productos/templates/detalle_producto.html"
    context_object_name = "producto"



class ProductoCreateView(CreateView):
    model = Productos
    form_class = ProductoForm 
    template_name = "productos/templates/formulario_producto.html"
    success_url = reverse_lazy("lista-productos")



class ProductoUpdateView(UpdateView):
    model = Productos
    form_class = ProductoForm
    template_name = "productos/templates/formulario_producto.html"
    success_url = reverse_lazy("lista-productos")


class ProductoDeleteView(DeleteView):
    model = Productos
    template_name = "productos/templates/confirmar_borrado.html"
    success_url = reverse_lazy("lista-productos")
