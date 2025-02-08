import json

################################################################################################################################################
#general
################################################################################################################################################

def validar_opcion(enunciando,inferior,superior):
    while True:
        try:
            opcion =int(input(enunciando))
            if opcion>=inferior and opcion<=superior:
                return opcion
            else:
                print(f"Opción no está entre el intervalo de ({inferior}-{superior})")
        except ValueError:
            print("Por favor, introduce un número válido. ")

def load_json(archivo): 
    with open(archivo, 'r', encoding="utf-8") as archivo_json:        
            lista_campers = json.load(archivo_json)
            return lista_campers

def validar_login(archivo, username, password, tipo):

    if tipo == "camper":
        dataEntidades = load_json(archivo)
    
        if dataEntidades["Campers"]:
            for camper in dataEntidades["Campers"]:
                if camper["nombres"] == username and camper["id"] == password:
                    return True
        else:
            print("No hay campers registrados.")
            return False

    elif tipo == "trainer":
        trainers = load_json(archivo)
    
        if trainers["Trainers"]:
            for trainer in trainers["Trainers"]:
                if trainer["nombre"] == username and trainer["id"] == password:
                    return True
        else:
            print("No hay trainers registrados.")
            return False
    elif tipo == "coordinador":
        coordinadores = load_json(archivo)
    
        if coordinadores["Coordinadores"]:
            for coordinador in coordinadores["Coordinadores"]:
                if coordinador["nombre"] == username and coordinador["id"] == password:
                    return True
        else:
            print("No hay coordinadores registrados.")
            return False
        
def clearScreen():
    import os
    os.system('cls' if os.name == 'nt' else 'clear') 
    return


