# Desarrollo Web con Python Flask

Flask es el pegamento del curso. Nos permitirá integrar todo lo que sabemos de desarrollo Front-End (HTML-CSS-Bootstrap) y lo integraremos con los conocimientos de Back-End (SQL-Python) para realizar aplicaciones Full-Stack (Back-End + Front-End)

## Pipenv

Cada proyecto web tiene sus propias dependencias que deben permanecer aisladas para no causar conflictos cuando se trabaja en más de un proyecto en el mismo entorno de desarrollo. Para lograr esto existen varias alternativas, en el mundo Python no existe un consenso sobre qué enfoque utilizar. Para este curso utilizaremos la herramienta [Pipenv](https://pipenv.pypa.io/en/latest/).

Pipenv crea y maneja automáticamente los diferentes entornos que tenemos en nuestro computador de desarrollo. Estos entornos se conocen como *virtualenv*.

![pipenv en mac]()

### Instalación

Para instalar Pipenv necesitamos estar seguros de contar con Python y la herramienta `pip`. Revisaremos esto con los siguientes comandos en la terminal **Powershell**:

`python -V`

`pip -V`

En ambos casos debería retornar un número de versión similar a lo siguiente:

`Python 3.6.9`

`pip 21.3 from /usr/local/lib/python3.6/dist-packages/pip (python 3.6)`

Ahora con la herramienta `pip` (herramienta estándar para instalar librerías en Python) instalaremos `pipenv` (que maneja las librerías separadas por proyecto usando Virtual Environments o Virtualenvs o Entornos Virtuales, que son lo mismo).

`pip install --user pipenv`

Luego, para utilizar el comando  `pipenv`, debemos actualizar la variable del sistema `PATH`. Esta variable específica las rutas que el sistema busca para ejecutar los comandos que usamos en la terminal.

Buscar el editor de variables de entorno del **Sistema**.

1. Dirígete al buscador de aplicaciones
2. Busca por "variables"
3. Clic en: Editar las variables de entorno del sistema

Luego, en la parte inferior da click y selecciona la variable `Path` (1 en la siguiente imagen) y a continuación Editar (2 en la siguiente imagen).

En el siguiente cuadro de diálogo haz clic en Nuevo y agregar una a la vez las siguientes rutas:

```bash
C:\Users\<username>\AppData\Roaming\Python\Python38\Site-Packages
```

```bash
C:\Users\<username>\AppData\Roaming\Python\Python38\Scripts
```

>**ATENCIÓN**: Asegúrate de reemplazar <username> por tú nombre de usuario. Si no lo recuerdas, puedes revisarlo discretamente en `gitbash`
>**ATENCIÓN II**: Puede que tu carpeta de python se llame diferente por la versión específica. Revisa navegando en las carpetas para corroborar si es Python38 u otra.


Luego de esto debemos reiniciar Powershell.

Podemos revisar que todo salió bien ejecutando el siguiente comando:

`pipenv -h`

Si todo salió bien en la salida deberías ver un resumen de como usar `pipenv`

¡Buen trabajo!


## Extensiones
Instalar dependencias

`pipenv install`

## Correr las migraciones

`flask db upgrade`

## Levantar el servidor de desarrollo.
Con todo esto

```bash
pipenv shell
pipenv install
set FLASK_APP=app
set FLASK_ENV=development
flask run
```
O con la siguiente línea

`pipenv run flask --app app --debug run`

Y si tiene el archivo .env con las variables FLASK_DEBUG=1 y FLASK_APP=app, solo debe ejecutar lo siguiente

`flask run`

## Blueprints

## MVC (Model-View-Controller)

![MVC](https://cdn.educba.com/academy/wp-content/uploads/2019/04/what-is-mvc-design-pattern.jpg.webp)

Es una arquitectura para separar las responsabilidades en la manipulación de las solicitudes y respuestas. Quien recibe las solicitudes es el Controlador o en flask, las rutas. Los controladores se encargan de revisar que la solicitud cumpla con las características necesarias para entregar una respuesta acorde (que tenga todos los datos). Si el controlador lo permite, se podría opcionalmente llamar al modelo para obtener o modificar los datos de la BBDD. Y finalmente enviar una respuesta que contenga la presentación de la aplicación. En nuestro caso la capa de presentación comúnmente conocida como Vistas (views) se llaman Templates. 

Por lo tanto en Flask el MVC podría ser adaptado como MTR (Modelo, Template, Ruta), pero es lo mismo en términos de separar la responsabilidad.

