# Seguimiento Academico para Campers

Este proyecto es una aplicación de consola en Python que gestiona la información de campers, trainers y coordinadores. El sistema permite registrar, consultar, calificar y organizar a los estudiantes en rutas de formación y grupos, utilizando archivos JSON para el almacenamiento de datos.

## Estructura de Archivos

El proyecto se compone de varios archivos JSON que actúan como base de datos, y un script principal en Python (interfaz.py) que maneja toda la lógica del programa:

* ```interfaz.py:``` El script principal que contiene la interfaz de usuario de la aplicación.

* ```estudiantes.json:``` Almacena los datos de los campers, incluyendo su información personal, estado y riesgo.

* ```trainers.json:``` Contiene la información de los trainers, incluyendo su nombre, apellido y la ruta de formación a la que están asignados.

* ```coordinador.json:``` Almacena los datos del coordinador del programa.

* ```rutas.json:``` Define las diferentes rutas de formación disponibles, como "Java", "NodeJS" y ".Net", y los módulos que cada una incluye.

* ```salones.json:``` Lista los salones disponibles, como "Atermis", "Apollo" y "Sputnik".

* ```horarios.json:``` Define los horarios para los grupos de estudio.

* ```grupo.json:``` Organiza los grupos de estudiantes, asignándoles un salón, un trainer, un horario y una ruta específica.

* ```notas.json:``` Guarda las notas de los estudiantes por cada módulo de las rutas, incluyendo calificaciones de proyectos, filtros, trabajos y el resultado final.

## Funcionalidades

El sistema ofrece diferentes perfiles de usuario, cada uno con funcionalidades específicas:

1. Perfil del Camper

* Iniciar Sesión/Registrarse: Los campers pueden iniciar sesión con su nombre e ID, o registrarse como nuevos estudiantes.

* Ver Información: Pueden consultar sus datos personales, incluyendo su estado y nivel de riesgo.

* Ver Notas: Les permite ver las notas obtenidas en cada módulo de su ruta.

2. Perfil del Trainer

* Ver Información: Los trainers pueden consultar su propia información y la ruta que tienen asignada.

* Calificar Estudiantes: Tienen la capacidad de asignar notas a los estudiantes en módulos específicos. El sistema calcula el resultado final (60% proyecto, 30% filtro, 10% trabajos) y actualiza el estado de riesgo del estudiante si la nota es menor a 60.

* Ver Estudiantes: Pueden ver el listado completo de todos los estudiantes.

3. Perfil del Coordinador

* Gestión de Perfiles: Puede ver y editar la información de campers, trainers y otros coordinadores.

* Reportes: Puede generar reportes de estudiantes en diferentes estados (aprobado, en riesgo, etc.), así como ver los trainers y campers asignados a cada salón.

* Gestión de Grupos y Rutas: Funcionalidades para manejar la asignación de estudiantes a grupos, horarios y rutas de formación.

## Cómo Ejecutar el Proyecto

* Asegúrate de tener Python instalado en tu sistema.

* Clona o descarga este repositorio.

* Abre una terminal o línea de comandos.

* Navega hasta el directorio del proyecto.

* Ejecuta el script principal con el siguiente comando:

```
python3 interfaz.py
```

* Sigue las instrucciones en pantalla para seleccionar un perfil e interactuar con el sistema.


## Creditos

### Sergio Rueda
