def promedio_plan():
    efectividad/cont_planes

cont_planes=0
lista=[[],
       []]
Categoría=""
while True:
    print("------MENU------\n")
    print("1.- Agregar plan")
    print("2.- Lista de planes")
    print("3.- Eliminar plan")
    print("4.- Generar bbdd")
    print("5.- Cargar bbdd")
    print("6.- Estadisticas")
    print("0.- Salir\n")
    op=int(input("Ingrese una opcion : "))
    
    if op==1:
            print("-----"*20)
            print("-----AGREGANDO PLANES-----\n")
            Id=int(input("Ingrese Id del plan : "))
            nombre=input("Ingrese el nombre del plan : ")
            efectividad=int(input("Ingrese el porcentaje de efectividad : "))
            if efectividad<=0 and efectividad>=25:
                Categoría="Chiste"
            if efectividad<=26 and efectividad>=50:
                Categoría="Anécdota"
            if efectividad<=51 and efectividad>=75:
                Categoría="Peligro"
            if efectividad<=76 and efectividad>=99:
                Categoría="Atención"
            if efectividad==100:
                Categoría="Esclavitud"    
            lista=("Id :",Id, "Nombre :",nombre, "Porcentaje :",efectividad,Categoría)            
            print(lista)
            
    elif op==2:
        print("-----"*20)
        print("--------LISTA DE PLANES--------\n")
        for planes in lista:
            print(lista)
    elif op==3:
        encontrado=False
        print("")
        print("--------ELIMINANDO PLAN----------\n")
        Id=int(input("Ingrese Id del plan : "))
        if encontrado==True:
            for planes in lista:
                lista.remove
                print(lista)
                print("Plan eliminado correctamente")
    elif op==4:
        print("------"*20)
        print("--------Generando bbdd--------\n")
        with open ('lista_planes.csv','w',newline='') as lista_planes:
            writer.writerow()     
    elif op==5:
        print("------"*20)
        print("-----Cargar bbdd-------\n")
    elif op==6:
        print("------"*20)
        print("------Estadisticas-------\n")
        print("1.- Porcentaje de efectividad promedio : ",promedio_plan)
        print("2.- Plan con el porcentaje mas alto de efectividad : ")
    elif op==0:
        print("Adiooooosss")
        break