# productos/forms.py
from django import forms
from .models import Productos


class ProductoForm(forms.ModelForm):
    class Meta:
        model = Productos
        # Define los campos que aparecerán en tu formulario
        fields = ["nombre", "descripcion", "precio", "disponible"]

        # Opcional: puedes personalizar los widgets para que se vean mejor
        widgets = {
            "nombre": forms.TextInput(attrs={"class": "form-control"}),
            "descripcion": forms.Textarea(attrs={"class": "form-control", "rows": 3}),
            "precio": forms.NumberInput(attrs={"class": "form-control"}),
            "disponible": forms.NumberInput(attrs={"class": "form-control"}),
        }
