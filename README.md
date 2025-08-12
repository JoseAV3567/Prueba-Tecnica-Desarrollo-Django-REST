# Prueba-Tecnica-Desarrollo-Django-REST
Perfecto, te lo pongo adaptado **solo para Windows** y en un README listo para usar.

---

# Crear y Activar un Entorno Virtual en Python (Windows)

## 📌 Requisitos

* Tener **Python 3.6 o superior** instalado.
* Tener **pip** instalado (viene incluido con Python).
* Usar **PowerShell** o **CMD**.

---

## 🚀 Pasos

### 1️⃣ Verificar que Python está instalado

En **PowerShell** o **CMD**:

```bash
python --version
```

Debe mostrar algo como:

```
Python 3.10.6
```

---

### 2️⃣ Crear el entorno virtual

```bash
python -m venv .venv
```

> Esto creará una carpeta llamada `.venv` que contendrá el entorno.

---

### 3️⃣ Activar el entorno virtual

#### 🔹 En PowerShell

```powershell
.\venv\Scripts\Activate
```

#### 🔹 En CMD

```cmd
venv\Scripts\activate
```

### 4️⃣ Instalar Django

Con el entorno activado:

```bash
pip install django
```

---

### 5️⃣ Guardar dependencias en `requirements.txt`

```bash
pip freeze > requirements.txt
```

> Este archivo contiene todas las librerías y sus versiones, para que otros puedan instalarlas fácilmente.

---

### 6️⃣ Instalar dependencias desde `requirements.txt`

Si recibes un proyecto que ya tiene este archivo, instala todo con:

```bash
pip install -r requirements.txt
```

---
7️⃣ Crear y levantar el contenedor con Docker
Si tu proyecto está configurado con Docker y tiene un archivo docker-compose.yml, puedes construir y levantar el contenedor usando:

bash
Copiar
Editar
docker-compose up --build
Explicación del comando:

docker-compose → Herramienta para gestionar múltiples contenedores definidos en docker-compose.yml.

up → Crea e inicia los contenedores definidos.

--build → Fuerza la reconstrucción de la imagen antes de iniciar los contenedores (ideal si cambiaste código o dependencias).

💡 Tip: Ejecuta este comando en la misma carpeta donde se encuentra el archivo docker-compose.yml.
---
8️⃣ Ejecutar las migraciones iniciales (makemigrations)
Una vez que los contenedores estén corriendo, abre otra terminal (sin cerrar la que está ejecutando docker-compose up) y usa:

bash
Copiar
Editar
docker-compose exec web python manage.py makemigrations
Explicación:

docker-compose exec web → Ejecuta un comando dentro del contenedor llamado web (el nombre debe coincidir con el que está en tu docker-compose.yml).

python manage.py makemigrations → Detecta cambios en los modelos de Django y crea los archivos de migración necesarios.
---
9️⃣ Aplicar las migraciones
Después de crear las migraciones, aplícalas a la base de datos:

bash
Copiar
Editar
docker-compose exec web python manage.py migrate
Explicación:

python manage.py migrate → Aplica las migraciones creadas a la base de datos para que las tablas y campos estén actualizados.
---
1️⃣0️⃣ Crear un usuario administrador de Django
Para acceder al panel de administración de Django, necesitas crear un superusuario:

bash
Copiar
Editar
docker-compose exec web python manage.py createsuperuser
Explicación:

createsuperuser → Inicia un asistente interactivo donde debes ingresar usuario, email y contraseña.

Este usuario podrá acceder a http://localhost:8000/admin (o el puerto configurado) con los datos que definas.
---
1️⃣1️⃣ Acceder a la documentación Swagger
Si el proyecto tiene drf-yasg o alguna integración de Swagger/OpenAPI, podrás visualizar todas las rutas y probarlas desde el navegador:

Abre tu navegador.

Ve a la dirección:

bash
Copiar
Editar
http://localhost:8000/swagger/
---

## ⚡ Comandos Rápidos (Cheat Sheet)

```powershell
python -m venv venv
.\venv\Scripts\Activate   # PowerShell
pip install <paquete>
pip freeze > requirements.txt
deactivate
```

---

Si quieres, te lo puedo dejar **con formato bonito en Markdown con emojis y colores** para que quede pro en GitHub.
¿Quieres que lo haga así?
