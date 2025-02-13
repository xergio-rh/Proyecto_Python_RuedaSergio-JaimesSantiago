import json
from modulo import *
from menus import *
def abrirJSON(Ruta):
    dicFinal={}
    with open(f'./campers.json','r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal
zzz={}


def guardarJSON(dic,Ruta):
    with open(f"./campers.json",'w') as outFile:
        json.dump(dic,outFile)


def main_menu():
    lie = True  # Aseguramos que lie sea True para entrar en el bucle

    while lie:
        print("Seleccione el tipo de perfil")
        print("############### WELCOME TO #####################")
        print("############### CAMPUSLANDS #####################")
        print("--Inicia Sesion:")
        print("1 para campers || 2 para trainers || 3 para coordinador")

        try:
            seleccion = int(input(": "))  # Intentamos recibir un número entero
            
            if seleccion == 1:
                menu_campers()
                return  # Salimos de la función inmediatamente

            elif seleccion == 2:
                menu_trainers()
                return  

            elif seleccion == 3:
                menu_coordinador()
                return  

            else:
                print("⚠ Opción no válida, por favor seleccione de nuevo.\n")

        except ValueError:
            print("⚠ Entrada inválida. Ingrese un número (1, 2 o 3).\n")

# ✅ Corregimos menu_campers() para que maneje su propio flujo
def menu_campers():
    while True:
        print("\n### Menú Campers ###")
        print("1. Ver cursos")
        print("2. Ver notas")
        print("3. Salir al menú principal")

        try:
            opcion = int(input("Seleccione una opción: "))

            if opcion == 1:
                print("Mostrando cursos...")
                input("\nPresione Enter para volver al menú campers...")  

            elif opcion == 2:
                print("Mostrando notas...")
                input("\nPresione Enter para volver al menú campers...")

            elif opcion == 3:
                print("Volviendo al menú principal...")
                return  # Salimos de menu_campers() y regresamos a main_menu()

            else:
                print("⚠ Opción no válida. Inténtelo de nuevo.")

        except ValueError:
            print("⚠ Entrada inválida. Ingrese un número válido.")

def menu_coordinador ():
    while True:
        print("\n### Menú coordinador ###")
        print("1. Ver campers que se encuentren en estado de inscrito.")
        print("2. Ver  campers que aprobaron el examen inicial.")
        print("3. Ver entrenadores que se encuentran trabajando con CampusLands.")
        print("4. Ver campers que cuentan con bajo rendimiento.")
        print("5. Ver campers y trainers que se encuentren asociados a una ruta de entrenamiento.")
        print("6. Mostrar cuantos campers perdieron y aprobaron cada uno de los módulos teniendo en cuenta la ruta de entrenamiento y el entrenador encargado.")
        print("########--Elige una opcion--######")
        optt=int(input(":"))
        
        if optt==1:
          print(listar_campers_inscritos ())
        elif optt==2:
            
          main_menu()





                
                
        


        
        






















































        
   # if opc==3:#
    #    menu_coordinador()#
     #   asignacion=int(input(": "))#




""" elif opc ==2:
                print("Ingrese su numero de documeto:")
                id=input(":")
                print("Ingrese su nombre:")
                name=input(":")
                print("Ingrese su apellido:")
                lastname=input(":")
                print("Ingrese su direccion")
                direccion=input(":")
                print("Ingrese el nombre de su acudiente:")
                acudiente=input(":")
                print("Ingrese su numero de telefono:")
                telefono=input(":")
                print("Ingrese su estado (En proceso de ingreso, Inscrito, Aprobado,Cursando, Graduado, Expulsado, Retirado):")
                estado=input(":")
        
            if id in data [ "campers"]:
                print("El estudiante ya esta registrado")
            else:
                data["campers"].append({
                    "id": id,
                    "nombres": name,
                    "apellidos": lastname,
                    "direccion": direccion,
                    "acudiente": acudiente,
                    "telefono": telefono,
                    "estado": estado, 
                    "riesgo": ""})
                guardarJSON(data)"""
        