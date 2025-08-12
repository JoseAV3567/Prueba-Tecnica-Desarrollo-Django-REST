# productos/swagger.py

from django.urls import re_path
from rest_framework import permissions
from drf_yasg.views import get_schema_view
from drf_yasg import openapi

# This creates a schema view for your API.
# The openapi.Info object provides metadata about your API.
schema_view = get_schema_view(
    openapi.Info(
        title="Credenciales API",
        default_version="v1",
        description="API Rest para la gestión de Productos",
        contact=openapi.Contact(email="213233@uptapachulas.edu.mx"),
        license=openapi.License(name="License Jose"),
    ),
    public=True,
    permission_classes=[permissions.AllowAny],
)

# These are the URL patterns for the documentation endpoints.
urlpatterns = [
    # URL for the raw schema in JSON or YAML format
    re_path(
        r"^swagger(?P<format>\.json|\.yaml)$",
        schema_view.without_ui(cache_timeout=0),
        name="schema-json",
    ),
    # URL for the interactive Swagger UI
    re_path(
        r"^swagger/$",
        schema_view.with_ui("swagger", cache_timeout=0),
        name="schema-swagger-ui",
    ),
    # URL for the ReDoc documentation UI
    re_path(
        r"^redoc/$",
        schema_view.with_ui("redoc", cache_timeout=0),
        name="schema-redoc",
    ),
]
