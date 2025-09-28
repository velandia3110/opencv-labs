# 🖼️ Laboratorio 1 – OpenCV  

Este proyecto contiene ejemplos de procesamiento de imágenes en **Python + OpenCV**.  

## 🚀 Requisitos  
- Python **3.11** (recomendado)  
- Git (opcional, si quieres clonar el repositorio)  

---

## ⚙️ 1. Crear un entorno virtual  

En la carpeta raíz del proyecto:  

```bash
python -m venv venv
```

Esto creará una carpeta llamada **venv/** que contendrá tu entorno virtual.  

---

## ▶️ 2. Activar el entorno virtual  

- **Windows (CMD):**  
  ```bash
  venv\Scripts\activate
  ```

- **Windows (PowerShell):**  
  ```powershell
  .\venv\Scripts\Activate
  ```

- **Linux/MacOS:**  
  ```bash
  source venv/bin/activate
  ```

Cuando el entorno esté activo, verás algo como:  
```bash
(venv) C:\Users\julia\...\lab I>
```

---

## 📦 3. Instalar dependencias  

Con el entorno activado:  
```bash
pip install -r requirements.txt
```

Si no tienes el archivo `requirements.txt`, instala manualmente:  
```bash
pip install opencv-python matplotlib numpy pydicom
```

---

## ▶️ 4. Ejecutar el proyecto  

Para correr el script principal:  

```bash
python main.py
python img_dicom_script.py # para el punto 9 del lab I
```
No olvides ingresar a la carpeta donde esté el script necesario.
---

## ❌ 5. Desactivar el entorno virtual  

Cuando termines, puedes salir del entorno con:  
```bash
deactivate
```

---

### 📌 Notas  
- Si usas **VS Code**, selecciona el kernel de Python correspondiente al entorno virtual (`venv`).  
- Si algún paquete tarda demasiado en instalarse, prueba:  
  ```bash
  pip install --default-timeout=100 opencv-python
  ```  
