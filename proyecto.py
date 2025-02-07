import json

def abrirJSON(datos):
    Datos ={}
    with open(f"./datos.json",'r') as openFile:
        Datos_de_campus=json.load(openFile)
    return Datos_de_campus

def guardarJSON(datos):
    with open(f"./datos.json",'w') as outFile:
        json.dump(datos,outFile)




print("####MENU#####")
print("##Bienvenidos a Campus ##")
print("1. Ingresa o registrate como camper:")
print("2. Ingresar como trainer")
print("3. Ingresar como coordinador")

Booleanito=True
while Booleanito==True:
    print("1. ver lista de estudiantes")
    opt=int(input(":"))
    



    