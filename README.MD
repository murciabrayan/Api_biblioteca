# API Biblioteca

API REST construida con **Django** y **Django REST Framework** para la gestión de autores, editoriales, libros, miembros y préstamos.


El proyecto utiliza las siguientes dependencias:

```
asgiref==3.9.1
Django==5.2.6
djangorestframework==3.16.1
psycopg2==2.9.10
sqlparse==0.5.3
tzdata==2025.2
```


# Crear y activar un entorno virtual

```bash
python -m venv venv
source venv/bin/activate  
venv\Scripts\activate      

# Instalar dependencias

```bash
pip install -r requirements.txt
```

# Aplicar migraciones
```bash
python manage.py migrate
```

# Ejecutar el servidor
```bash
python manage.py runserver
```

El enlace del servidor es: 
 **http://127.0.0.1:8000**



## 🚀 Endpoints principales

- **Autores:** `/api/autores/`
- **Editoriales:** `/api/editoriales/`
- **Libros:** `/api/libros/`
- **Miembros:** `/api/miembros/`
- **Préstamos:** `/api/prestamos/`


Documentacion de Postman:
https://documenter.getpostman.com/view/48002548/2sB3HkrgSz

