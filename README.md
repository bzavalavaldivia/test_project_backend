# Test Project ![CI status](https://img.shields.io/badge/build-passing-brightgreen.svg)

Prueba de sistema de encuestas.

## Installation

### Requirements
* Git
* Python >= 3.9.1
* MySQL o MariaDB

## Pasos
```
$ git clone https://github.com/bzavalavaldivia/test_project.git
$ cd test_project
$ pip install -r requirements.txt

Crea una copia de los siguientes archivos:

test_project/settings/local.py.example a test_project/settings/local.py
test_project/settings/production.py.example a test_project/settings/production.py

Configura el archivo test_project/settings/local.py o production.py con la información de tu base de datos.

$ python manage.py makemigrations
$ python manage.py migrate
```

## Uso

Es una aplicación que te permite crear encuentas con preguntas de diferentes tipos.

```
Para poder acceder al panel de administración crea un superusuario con el siguiente comando:

$ python manage.py createsuperuser

Para correr el servidor en modo local ejecuta el siguiente comando:

$ python manage.py runserver
```

Enlance para ingresar al panel de administración: http://localhost:8000/admin/
