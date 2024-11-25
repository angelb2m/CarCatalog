
# 🚗 **Catálogo de Autos - API REST**

API REST para la gestión y consulta de un catálogo de autos. Este proyecto permite listar, filtrar, buscar y ordenar autos mediante peticiones HTTP con métodos exclusivamente de lectura (`GET`).

---

## 📚 **Descripción del Proyecto**

Proyecto realizado para la clase de **Tecnologías de Construcción de Servicios Web**.  
**Universidad del Valle de México (UVM)** - 2024.  
**Profesor:** José Antonio Urquidez Ramírez.

Este proyecto implementa un catálogo de autos utilizando **Django REST Framework (DRF)** y permite:

- Consultar una lista de autos.
- Aplicar filtros por campos como marca, año, precio, tipo de combustible, entre otros.
- Ordenar resultados por precio, año, kilometraje, etc.
- Buscar autos en base a palabras clave en la descripción o el modelo.

---

## 🚀 **Tecnologías Utilizadas**

- **Backend:** Django, Django REST Framework
- **Base de Datos:** SQLite (por defecto, fácilmente reemplazable)
- **Lenguaje:** Python
- **Dependencias:**
  - `django-filter` para filtros avanzados.
  - `Faker` para la generación de datos de ejemplo.

---

## 🛠️ **Configuración del Proyecto**

### **1. Clonar el Repositorio**
```bash
git clone https://github.com/angelb2m/CarCatalog.git
cd CarCatalog
```

### **2. Crear un Entorno Virtual**
```bash
python -m venv venv
source venv/bin/activate  # En Windows: venv\Scripts\activate
```

### **3. Instalar Dependencias**
```bash
pip install -r reqs.txt
```

### **4. Aplicar las Migraciones**
```bash
python manage.py makemigrations
python manage.py migrate
```

### **5. Generar Datos de Ejemplo**
```bash
python manage.py seed_cars
```

### **6. Ejecutar el Servidor**
```bash
python manage.py runserver
```

---

## 📖 **Uso de la API**

### **Listar Autos**
```http
GET /api/cars/
```

### **Filtrar Autos**
Por marca y precio:
```http
GET /api/cars/?brand=Toyota&price__lte=20000
```

### **Ordenar Autos**
Por precio ascendente:
```http
GET /api/cars/?ordering=price
```

### **Buscar Autos**
Buscar en la descripción o modelo:
```http
GET /api/cars/?search=deportivo
```

### **Detalles de un Auto**
```http
GET /api/cars/<id>/
```

---

## 📂 **Estructura del Proyecto**
```
car_catalog/
├── car_catalog/
│   ├── settings.py
│   ├── urls.py
│   └── ...
├── cars/
│   ├── migrations/
│   ├── models.py
│   ├── serializers.py
│   ├── views.py
│   ├── urls.py
│   └── ...
├── db.sqlite3
├── manage.py
└── README.md
```

---

## 📜 **Licencia**

Este proyecto se encuentra bajo la licencia MIT. Puedes consultar el archivo [LICENSE](LICENSE) para más detalles.

---

## 👨‍🏫 **Créditos**

- **Autor:** [Angel Nunez](https://github.com/angelb2m)
- **Profesor:** José Antonio Urquidez Ramírez  
- **Clase:** Tecnologías de Construcción de Servicios Web  
- **Institución:** Universidad del Valle de México (UVM)  
- **Año:** 2024
