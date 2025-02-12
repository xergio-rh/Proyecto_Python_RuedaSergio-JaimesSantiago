import json



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
        opc = int(input(":"))
        data= {}
        def abrirJSON(campers):
            if opc == 1:
                menu_campers ()
            elif opc ==2:
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
                guardarJSON(data)
                    


                
                
        


        
        














































eli=True
while eli==True:   
        Opc = input()    
        if opc==2:
            menu_trainers()
        eli = False








        
   # if opc==3:#
    #    menu_coordinador()#
     #   asignacion=int(input(": "))#
        