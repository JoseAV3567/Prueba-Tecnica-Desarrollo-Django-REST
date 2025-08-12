from django.contrib import admin
from productos.models import *


@admin.register(Productos)
class TreasuryAdmin(admin.ModelAdmin):
    list_display = ["__str__", "nombre", "descripcion"]
    list_filter = ["disponible"]
    search_fields = [
        "nombre",
    ]
