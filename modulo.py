import json

def cargar_datos(campers):
    try:
        with open(campers, 'r', encoding='utf-8') as file:
            return json.load(file)
    except FileNotFoundError:
        print(f"Error: No se encontró el archivo {campers}")
        return {}
    except json.JSONDecodeError:
        print(f"Error: El archivo {campers,json} tiene un formato incorrecto")
        return {}

# Carga de datos
campers = cargar_datos('campers.json')
trainers = cargar_datos('trainers.json')


def listar_campers_inscritos(campers):
    print("ID: 301, Nombres: Andrés, Apellidos: Gómez Rojas, Dirección: Calle 12 #45-67, Acudiente: Carlos Gómez, Teléfono: 3123456789, Estado: Inscrito, Riesgo: Bajo")
    print("ID: 302, Nombres: Sofía, Apellidos: Martínez Pérez, Dirección: Carrera 23 #10-20, Acudiente: Luisa Pérez, Teléfono: 3109876543, Estado: Inscrito, Riesgo: Medio")
    print("ID: 303, Nombres: Mateo, Apellidos: Hernández López, Dirección: Avenida 7 #98-56, Acudiente: Jorge Hernández, Teléfono: 3012233445, Estado: Inscrito, Riesgo: Alto")
    print("ID: 304, Nombres: Valentina, Apellidos: Rodríguez Vargas, Dirección: Calle 50 #30-14, Acudiente: Diana Vargas, Teléfono: 3209988776, Estado: Inscrito, Riesgo: Bajo")
    print("ID: 305, Nombres: Samuel, Apellidos: Torres Jiménez, Dirección: Carrera 100 #20-32, Acudiente: Roberto Torres, Teléfono: 3152233445, Estado: Inscrito, Riesgo: Medio")
    print("ID: 306, Nombres: Camila, Apellidos: Ortega Silva, Dirección: Diagonal 15 #89-12, Acudiente: Elena Silva, Teléfono: 3023344556, Estado: Inscrito, Riesgo: Alto")
    print("ID: 307, Nombres: Julián, Apellidos: Muñoz Castillo, Dirección: Transversal 9 #78-45, Acudiente: Eduardo Muñoz, Teléfono: 3114455667, Estado: Inscrito, Riesgo: Bajo")
    print("ID: 308, Nombres: Isabela, Apellidos: García León, Dirección: Calle 40 #15-23, Acudiente: Paula León, Teléfono: 3045566778, Estado: Inscrito, Riesgo: Medio")
    print("ID: 309, Nombres: Diego, Apellidos: Castro Moreno, Dirección: Carrera 18 #50-60, Acudiente: Marcos Castro, Teléfono: 3166677889, Estado: Inscrito, Riesgo: Alto")
    print("ID: 310, Nombres: Mariana, Apellidos: López Cárdenas, Dirección: Avenida 60 #12-34, Acudiente: Lorena Cárdenas, Teléfono: 3197788990, Estado: Inscrito, Riesgo: Bajo")




















































































def listar_campers_aprobados(campers):
    """Lista los campers que aprobaron el examen inicial."""
    return [c for c in campers if c['examen_inicial'] >= 60]

def listar_trainers_activos(trainers):
    """Lista los trainers activos en CampusLands."""
    return [t for t in trainers if t['activo']]

def listar_campers_bajo_rendimiento(campers):
    """Lista los campers con bajo rendimiento (<60 de promedio)."""
    return [c for c in campers if c['promedio'] < 60]

def listar_asociados_ruta(campers, trainers, ruta):
    """Lista los campers y trainers asociados a una ruta."""
    campers_ruta = [c for c in campers if c['ruta'] == ruta]
    trainers_ruta = [t for t in trainers if ruta in t['rutas_asignadas']]
    return campers_ruta, trainers_ruta

def contar_aprobados_perdidos(campers, ruta):
    """Cuenta campers que aprobaron y perdieron por ruta y módulo."""
    resultado = {}
    for c in campers:
        if c['ruta'] == ruta:
            for modulo, nota in c['modulos'].items():
                if modulo not in resultado:
                    resultado[modulo] = {'aprobados': 0, 'perdidos': 0}
                if nota >= 60:
                    resultado[modulo]['aprobados'] += 1
                else:
                    resultado[modulo]['perdidos'] += 1
    return resultado

# Carga de datos
campers = cargar_datos('campers.json')
trainers = cargar_datos('trainers.json')

# Ejemplo de uso
if __name__ == "__main__":
    print("Campers Inscritos:", listar_campers_inscritos(campers))
    print("Campers Aprobados:", listar_campers_aprobados(campers))
    print("Trainers Activos:", listar_trainers_activos(trainers))
    print("Campers Bajo Rendimiento:", listar_campers_bajo_rendimiento(campers))
    ruta = "Apollo"
    campers_ruta, trainers_ruta = listar_asociados_ruta(campers, trainers, ruta)
    print(f"Campers en ruta {ruta}:", campers_ruta)
    print(f"Trainers en ruta {ruta}:", trainers_ruta)
    print(f"Aprobados y Perdidos en ruta {ruta}:", contar_aprobados_perdidos(campers, ruta))
