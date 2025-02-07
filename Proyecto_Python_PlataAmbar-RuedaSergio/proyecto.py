import json

def abrirJSON(datos):
    Datos ={}
    with open(f"./datos.json",'r') as openFile:
        Datos_de_campus=json.load(openFile)
    return Datos_de_campus

def guardarJSON(datos):
    with open(f"./datos.json",'w') as outFile:
        json.dump(datos,outFile)


def menu ():


print("####MENU#####")
print("##Bienvenidos a Campus ##")
print("1. Ingresa o registrate como camper:")
print("2. Ingresar como trainer")
print("3. Ingresar como coordinador")

   
opt =input(":")

    if opt ==1:
    print("1. Inicia sesion")
    print("2. Registrate")
    opt=(input(":"))
     
     elif

     opt == 1
        print("ingresa tu ID")
    elif
     opt == 2
        print("Ingresa tu nombre")
        input(" : ")

    return


menu()


    