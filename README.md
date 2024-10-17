# Django CRUD Project - Function-Based Views
Este proyecto es un ejemplo básico de un sistema CRUD (Create, Read, Update, Delete) construido en Django utilizando vistas basadas en funciones.

### Requisitos
Antes de comenzar, asegúrate de tener instalados los siguientes requisitos:

Python 3.x
Django 4.x
Bootstrap 4 (para el estilo de los formularios)
Crispy Forms (opcional, para mejorar el diseño de los formularios)
Instalación

### Clona el repositorio:

git clone https://github.com/tu-usuario/django-crud.git
cd django-crud

### Crea un entorno virtual y actívalo:
python -m venv venv
source venv/bin/activate  # Para Linux/MacOS
venv\Scripts\activate  # Para Windows

### Instala las dependencias:
pip install -r requirements.txt

### Realiza las migraciones:
python manage.py migrate

### Inicia el servidor de desarrollo:
python manage.py runserver

### Estructura del Proyecto

    django-crud/
    │
    ├── todoproject/
    │   ├── templates/
    │   │   ├── layout.html
    │   │   └── todoapp/
    │   │       ├── todo.html
    │   │       ├── show.html
    │   │       └── confirmation.html
    │   ├── todoapp/
    │   │   ├── forms.py
    │   │   ├── models.py
    │   │   ├── views.py
    │   │   └── urls.py
    │   ├── manage.py
    │   ├── settings.py

### Funcionalidad
El proyecto incluye las siguientes vistas:
Crear ToDo: Crea una nueva tarea.
Leer ToDos: Muestra una lista de todas las tareas.
Actualizar ToDo: Permite modificar una tarea existente.
Eliminar ToDo: Confirma y elimina una tarea.
URLs
