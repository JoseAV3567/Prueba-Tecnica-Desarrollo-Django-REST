Claro, aquí te dejo el README formateado de manera limpia, profesional y con emojis para que quede atractivo en GitHub. Usé bloques de código bien formateados, separadores claros, íconos para destacar, y una estructura fácil de seguir:

````markdown
# 🚀 Prueba Técnica Desarrollo Django REST (Windows)

¡Perfecto! Aquí tienes un README adaptado **solo para Windows**, listo para usar.

---

## 🐍 Crear y Activar un Entorno Virtual en Python (Windows)

### 📋 Requisitos

- Python 3.6 o superior instalado.
- pip (viene con Python).
- Usar PowerShell o CMD.

---

## 🛠 Pasos

### 1️⃣ Verificar que Python está instalado

Abre PowerShell o CMD y ejecuta:

```bash
python --version
````

Deberías ver algo así:

```
Python 3.10.6
```

---

### 2️⃣ Crear el entorno virtual

```bash
python -m venv .venv
```

> Esto crea una carpeta `.venv` con el entorno virtual.

---

### 3️⃣ Activar el entorno virtual

#### 🔹 PowerShell

```powershell
.\.venv\Scripts\Activate
```

#### 🔹 CMD

```cmd
.venv\Scripts\activate
```

---

### 4️⃣ Instalar Django

Con el entorno activado, ejecuta:

```bash
pip install django
```

---

### 5️⃣ Guardar dependencias en `requirements.txt`

```bash
pip freeze > requirements.txt
```

> Este archivo contiene todas las librerías instaladas con sus versiones.

---

### 6️⃣ Instalar dependencias desde `requirements.txt`

Si tienes un proyecto con este archivo, instala todo con:

```bash
pip install -r requirements.txt
```

---

### 7️⃣ Crear y levantar el contenedor con Docker

Si usas Docker y tienes `docker-compose.yml`, ejecuta:

```bash
docker-compose up --build
```

> **Explicación:**
>
> * `docker-compose`: gestiona múltiples contenedores.
> * `up`: crea e inicia los contenedores.
> * `--build`: fuerza reconstrucción de imágenes.

💡 Ejecuta este comando en la carpeta donde está `docker-compose.yml`.

---

### 8️⃣ Ejecutar migraciones iniciales

En otra terminal (sin cerrar Docker), ejecuta:

```bash
docker-compose exec web python manage.py makemigrations
```

> Detecta cambios en los modelos y crea archivos de migración.

---

### 9️⃣ Aplicar migraciones

Aplica los cambios a la base de datos con:

```bash
docker-compose exec web python manage.py migrate
```

---

### 🔟 Crear usuario administrador

Para crear un superusuario y acceder al panel admin:

```bash
docker-compose exec web python manage.py createsuperuser
```

> Sigue el asistente para definir usuario, email y contraseña.

Podrás entrar a: [http://localhost:8000/admin](http://localhost:8000/admin)

---

### 1️⃣1️⃣ Acceder a la documentación Swagger

Si usas Swagger/OpenAPI, abre en el navegador:

```
http://localhost:8000/swagger/
```

Aquí verás todas las rutas y podrás probarlas.

---

## ⚡ Comandos Rápidos (Cheat Sheet)

```powershell
python -m venv .venv
.\.venv\Scripts\Activate   # PowerShell
pip install <paquete>
pip freeze > requirements.txt
deactivate
```

---

