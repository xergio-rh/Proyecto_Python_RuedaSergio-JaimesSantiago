from menus import *
from utils import *

booleano = True
while booleano:

    op = log_type()

    match op:
        case 1:
            clearScreen()
            response = log_in("camper")
            if response:
                clearScreen()
                print("Login exitoso")
                opCamper = menu_camper()

                match opCamper:
                    case 1:
                        print("Perfil")
                    case 2:
                        print("Mi estado")
                    case 3:
                        print("Mis Aulas")
                    case 4:
                        get_camper_state(response) # Obtener el estado de un camper
                    case 5:
                        print("Saliendo...")
                        break
            else:
                print("Usuario o contraseña incorrecta.")
            break
        case 4:
            print("Saliendo del sistema...")
            booleano = False
            break
    