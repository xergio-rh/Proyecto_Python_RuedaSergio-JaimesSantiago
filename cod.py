import json
from menus import *
def abrirJSON(Ruta):
    dicFinal={}
    with open(f'./{Ruta}.json','r') as openFile:
        dicFinal=json.load(openFile)
    return dicFinal
zzz={}

def guardarJSON(dic,Ruta):
    with open(f"./{Ruta}.json",'w') as outFile:
        json.dump(dic,outFile)


lie=True
while lie==True:
    print("Seleccione el tipo de perfil")
    print("############### WELCOME TO #####################")
    print("############### CAMPUSLANDS #####################")
    print("--Inicia Sesion:")
    print("1 para campers || 2 para trainers || 3 para coordinador")
    seleccion=int(input(": "))
    if seleccion==1:
        menu_campers_registro ()
        ruta="campers"

        opc = int(input(":"))

        if opc == 1:
            menu_campers ()
        elif opc ==2:
            print ("Espere su registro")
        zzz=abrirJSON(ruta)


        lie=False 






























        1
    elif seleccion==2:
        menu_trainers()
        ruta="trainers"
        zzz=abrirJSON(ruta)
        lie = False
    if seleccion==3:
        menu_coordinador()
        asignacion=int(input(": "))
        ruta="coordinador"
        zzz={}
        zzz=abrirJSON(ruta)
        if asignacion==11:
            rta1="Cmapers"
            campers=abrirJSON(rta1)
            rta2="grupos"
            nombredeldiccionario=abrirJSON(rta2)
            salon=input("Ingrese el nombre del salon: ")
            id=int(input("Ingrese el id del estudiante a asginar: "))
            for i in range (len(campers["Campers"])):
                confirmacion=campers["Campers"][i]["id"]
                if confirmacion==id:
                    nombre=campers["Campers"][i]["nombres"]
                    apellidos=campers["Campers"][i]["apellidos"]
                    direccion=campers["Campers"][i]["direccion"]
                    acudiente=campers["Campers"][i]["acudiente"]
                    telefono=campers["Campers"][i]["telefono"]
                    estado=campers["Campers"][i]["estado"]
                    riesgo=campers["Campers"][i]["riesgo"]
            if salon=="s1":
                grupo=nombredeldiccionario[rta2][0][salon]["estudiantes"]
                grupo.append({"Nombre":nombre,"Apellido":apellidos,"direccion":direccion, "acudiente": acudiente, "telefono":telefono, "estado":estado, "riesgo": riesgo})
        
