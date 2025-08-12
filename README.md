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
python -m venv venv
```

> Esto creará una carpeta llamada `venv` que contendrá el entorno.

---

### 3️⃣ Activar el entorno virtual

#### 🔹 En PowerShell

```powershell
.\venv\Scripts\Activate
```

Si te da error de permisos, habilita la ejecución de scripts con:

```powershell
Set-ExecutionPolicy Unrestricted -Scope Process
```

y vuelve a ejecutar el comando de activación.

#### 🔹 En CMD

```cmd
venv\Scripts\activate
```

---

### 4️⃣ Instalar dependencias

Ejemplo:

```bash
pip install requests
```

---

### 5️⃣ Guardar dependencias

```bash
pip freeze > requirements.txt
```

---

### 6️⃣ Desactivar el entorno

```bash
deactivate
```

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
