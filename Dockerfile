# Usa una imagen base de Python oficial
FROM python:3.10-slim

# Establece variables de entorno
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# --- INICIO DE LA CORRECCIÓN ---
# Instala las dependencias del sistema necesarias para compilar mysqlclient
RUN apt-get update && apt-get install -y \
    pkg-config \
    build-essential \
    default-libmysqlclient-dev \
    && rm -rf /var/lib/apt/lists/*
# --- FIN DE LA CORRECCIÓN ---

# Establece el directorio de trabajo dentro del contenedor
WORKDIR /app

# Copia el archivo de requerimientos e instala las dependencias
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia todo el código del proyecto al directorio de trabajo
COPY . .

# Expone el puerto 8000 para que el servidor de Django sea accesible
EXPOSE 8000

CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]