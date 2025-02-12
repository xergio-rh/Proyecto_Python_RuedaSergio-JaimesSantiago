import json

# Funciones para manejo de archivos JSON
def abrir_JSON(ruta):
    try:
        with open(f"{ruta}.json", 'r') as file:
            return json.load(file)
    except FileNotFoundError:
        return {}

def guardar_JSON(ruta, data):
    with open(f"{ruta}.json", 'w') as file:
        json.dump(data, file, indent=4)

# CRUD CAMPERS
def agregar_camper():
    campers = abrir_JSON("campers")
    id_camper = input("Ingrese ID del camper: ")
    if id_camper in campers:
        print("El camper ya está registrado.")
        return
    nombre = input("Ingrese nombre del camper: ")
    campers[id_camper] = {"nombre": nombre, "curso": None, "notas": []}
    guardar_JSON("campers", campers)
    print("Camper agregado correctamente.")

def eliminar_camper():
    campers = abrir_JSON("campers")
    id_camper = input("Ingrese ID del camper a eliminar: ")
    if id_camper in campers:
        del campers[id_camper]
        guardar_JSON("campers", campers)
        print("Camper eliminado correctamente.")
    else:
        print("Camper no encontrado.")

def ver_campers():
    campers = abrir_JSON("campers")
    for id_camper, datos in campers.items():
        print(f"ID: {id_camper}, Nombre: {datos['nombre']}, Curso: {datos['curso']}")

# CRUD TRAINERS
def agregar_trainer():
    trainers = abrir_JSON("trainers")
    id_trainer = input("Ingrese ID del trainer: ")
    if id_trainer in trainers:
        print("El trainer ya está registrado.")
        return
    nombre = input("Ingrese nombre del trainer: ")
    trainers[id_trainer] = {"nombre": nombre, "rutas": []}
    guardar_JSON("trainers", trainers)
    print("Trainer agregado correctamente.")

def eliminar_trainer():
    trainers = abrir_JSON("trainers")
    id_trainer = input("Ingrese ID del trainer a eliminar: ")
    if id_trainer in trainers:
        del trainers[id_trainer]
        guardar_JSON("trainers", trainers)
        print("Trainer eliminado correctamente.")
    else:
        print("Trainer no encontrado.")

def ver_trainers():
    trainers = abrir_JSON("trainers")
    for id_trainer, datos in trainers.items():
        print(f"ID: {id_trainer}, Nombre: {datos['nombre']}")

# ASIGNACIONES
def asignar_curso_a_camper():
    campers = abrir_JSON("campers")
    id_camper = input("Ingrese ID del camper: ")
    if id_camper not in campers:
        print("Camper no encontrado.")
        return
    curso = input("Ingrese nombre del curso: ")
    campers[id_camper]["curso"] = curso
    guardar_JSON("campers", campers)
    print("Curso asignado correctamente.")

def asignar_trainer_a_ruta():
    trainers = abrir_JSON("trainers")
    id_trainer = input("Ingrese ID del trainer: ")
    if id_trainer not in trainers:
        print("Trainer no encontrado.")
        return
    ruta = input("Ingrese nombre de la ruta: ")
    trainers[id_trainer]["rutas"].append(ruta)
    guardar_JSON("trainers", trainers)
    print("Ruta asignada correctamente.")

# MENÚ PRINCIPAL
def menu_principal():
    while True:
        print("""
        1. Camper
        2. Trainer
        3. Coordinador
        4. Salir
        """)
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            menu_campers()
        elif opcion == "2":
            menu_trainers()
        elif opcion == "3":
            menu_coordinador()
        elif opcion == "4":
            break
        else:
            print("Opción no válida.")

# MENÚS SECUNDARIOS
def menu_campers():
    while True:
        print("""
        1. Ver curso asignado
        2. Ver notas
        3. Salir
        """)
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            ver_campers()
        elif opcion == "2":
            print("Función de ver notas pendiente.")
        elif opcion == "3":
            break
        else:
            print("Opción no válida.")

def menu_trainers():
    while True:
        print("""
        1. Ver campers
        2. Eliminar campers
        3. Asignar notas
        4. Salir
        """)
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            ver_campers()
        elif opcion == "2":
            eliminar_camper()
        elif opcion == "3":
            print("Función de asignar notas pendiente.")
        elif opcion == "4":
            break
        else:
            print("Opción no válida.")

def menu_coordinador():
    while True:
        print("""
        1. Ver trainers
        2. Ver campers
        3. Eliminar campers
        4. Eliminar trainers
        5. Agregar campers
        6. Agregar trainers
        7. Asignar curso a camper
        8. Asignar trainer a ruta
        9. Salir
        """)
        opcion = input("Seleccione una opción: ")
        if opcion == "1":
            ver_trainers()
        elif opcion == "2":
            ver_campers()
        elif opcion == "3":
            eliminar_camper()
        elif opcion == "4":
            eliminar_trainer()
        elif opcion == "5":
            agregar_camper()
        elif opcion == "6":
            agregar_trainer()
        elif opcion == "7":
            asignar_curso_a_camper()
        elif opcion == "8":
            asignar_trainer_a_ruta()
        elif opcion == "9":
            break
        else:
            print("Opción no válida.")

if __name__ == "__main__":
    menu_principal()
