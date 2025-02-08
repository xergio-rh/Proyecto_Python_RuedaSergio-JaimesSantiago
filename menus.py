from utils import validar_opcion, validar_login

def log_type():
    print(" _____WELCOME___")
    print("| 1.  Camper    |")
    print("|---------------|")
    print("| 2.  Trainer   |")
    print("|---------------|")
    print("| 3. Coordinador|")
    print("|_______________|")       
    op=validar_opcion("Opcion: ",1,3)
    return op

def log_in(tipo):
    print(" _____LOGEATE___")
    print("Nombre: ")
    nombre=str(input())
    print("Contraseña: ")
    password=int(input())

    result = validar_login("pp.json",nombre,password, tipo)
    return [result, password]



def menu_coordinador():
    print(" __COORDINADOR__")
    print("| 1. Campers    |")
    print("|---------------|")
    print("| 2. Trainers   |")
    print("|---------------|")
    print("| 3. Matriculas |")
    print("|---------------|")
    print("| 4. Aulas      |")
    print("|---------------|")
    print("| 5. Reportes   |")
    print("|---------------|")
    print("| 6. Salir      |")
    print("|_______________|")       
    op=validar_opcion("Opcion: ",1,6)
    return op


def menu_camper():
    print(" _____CAMPER____")
    print("| 1. Perfil     |")
    print("|---------------|")
    print("| 2. Mi estado  |")
    print("|---------------|")
    print("| 3. Mis Aulas  |")
    print("|---------------|")
    print("| 4. Mis notas  |")
    print("|---------------|")
    print("| 5. Salir      |")
    print("|_______________|")       
    op=validar_opcion("Opcion: ",1,6)
    return op

def menu_camper_co():
    print("________Campers_________")
    print("| 1. Crear campers     |")
    print("|----------------------|")
    print("| 2. listar campers    |")
    print("|----------------------|")
    print("| 3. Modificar campers |")
    print("|----------------------|")
    print("| 4. Salir             |")
    print("|______________________|")
    op=validar_opcion("Opcion: ",1,4)
    return op
    
    
def menu_trainer_co():
    print("________Trainers________")
    print("| 1. Crear trainer     |")
    print("|----------------------|")
    print("| 2. Buscar trainer    |")
    print("|----------------------|")
    print("| 3. Modificar trainer |")
    print("|----------------------|")
    print("| 4. Salir             |")
    print("|______________________|")
    op=validar_opcion("Opcion: ",1,4)
    return op

def menu_matriculas_co():
    print("_________Matriculas_______")
    print("|1. Crear Matriculas     |")
    print("|------------------------|")
    print("|2. Buscar Matriculas    |")
    print("|------------------------|")
    print("|3. Modificar Matriuclas |")
    print("|------------------------|")
    print("|4. Salir                |")
    print("|________________________|")
    op=validar_opcion("Opcion: ",1,4)
    return op

def menu_aulas_co():
    print("________Aulas________")
    print("|1. Crear Aulas     |")
    print("|-------------------|")
    print("|2. Buscar Aulas    |")
    print("|-------------------|")
    print("|3. Modificar Aulas |")
    print("|-------------------|")
    print("|4. Salir           |")
    print("|___________________|")
    op=validar_opcion("Opcion: ",1,4)
    return op

def menu_reportes_co():
    print("________________Reportes___________________")
    print("| 1. Listar campers estado inscripto      |")
    print("|-----------------------------------------|")
    print("| 2. Listar campers aprobaron examen      |")
    print("|-----------------------------------------|")
    print("| 3. Listar trainers trabajando en campus |")
    print("|-----------------------------------------|")
    print("| 4. Salir                                |")
    print("|_________________________________________|")
    op=validar_opcion("Opcion: ",1,4)
    return op