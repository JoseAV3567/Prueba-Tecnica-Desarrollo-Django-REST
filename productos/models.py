from django.db import models


class Productos(models.Model):
    """
    Modelo que representa un producto en el inventario.
    """

    nombre = models.CharField(max_length=255, verbose_name="Nombre")
    descripcion = models.TextField(
        verbose_name="Descripción", blank=True, null=True  # Campo opcional
    )
    precio = models.DecimalField(max_digits=10, decimal_places=2, verbose_name="Precio")
    disponible = models.BooleanField(
        default=True, verbose_name="Disponible"  # Valor por defecto es True
    )

    def __str__(self):
        return self.nombre

    class Meta:
        verbose_name = "Producto"
        verbose_name_plural = "Productos"
        ordering = ["nombre"]
