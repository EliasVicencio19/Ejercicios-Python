matriz = [[=0 for _ in range (7)]  for _ in range  (10)]
disponible=False
cont_columna=0
cont_fila=0

num=1
for i in range (10):
    for j in range (7):
        matriz [i][j]=num
        num = num+1
while True:
    try:
        print ("--------"*20)
        print ("")
        print (".-.-.-.-.-.-.-BIENVENIDO A CINE MARKIS.-.-.-.-.-.-.-") 
        print ("")
        print ("1.- Ver asientos disponibles")
        print ("2.- Comprar asientos")
        print ("3.- Ver cliente")
        print ("4.- Anular compra")
        print ("0.- Salir") 
        print("")
        op=int(input("Ingrese la opción que desea : ")) 
        
        if op==1:
                print("")
                print("-----------"*20)
                print("")
                print(".-.-.-.-.-.-.-ASIENTOS DISPONIBLES.-.-.-.-.-.-.-")
                print("")
                for fila in matriz:
                    for columna in fila:
                        print (columna, end=" ")
                    print("")
        elif op==2:
                print("")
                print(".-.-.-.-.-.-.-COMPRAR ASIENTOS.-.-.-.-.-.-.-")
                print("")
                for fila in matriz:
                    for columna in fila:
                        print(columna, end=" ")
                    print("")
                print("")
                asi=int(input("Ingrese el asiento que desea : "))    
                print("")
                for fila in matriz:
                    for columna in fila:
                        if columna!="X":
                             disponible=True
                             break
                        cont_columna=cont_columna
                    cont_fila=cont_fila+1
                    print("") 

        elif op==3:
            
        elif op==4:
            
        elif op==0:
             print("ADIOS!!!!")
             break
        else:
            print("Error...ingrese una opción valida...")
    except:
        print("Se ha producido un error!!!, redirigiendo al menu principal...")