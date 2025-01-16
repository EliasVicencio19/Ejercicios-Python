import random
import csv

luchadores = ['vegeta','gocku','trunks','krilin','gohan']
lista = []
l = []
for x in luchadores:
    l=[x]
    lista.append(l)

def asignar_ki():
    ki_a=random.randint(1000,100000)
    return ki_a

def asigna_categoria(ki_categoria):
    if ki_categoria>= 1000 and ki_categoria <=10000:
        categoria="terrícola"
    elif ki_categoria>10000 and ki_categoria<=50000:
        categoria="luchador"
    elif ki_categoria >50000 and ki_categoria<=100000:
        categoria="titan"
    return categoria

def imprimir(listita):
    print(".-.-.-Terricolas.-.-.-.\n")
    for x in listita:
        if x[2]=="terrícola":
            print(x)
    print(".-.-.-Luchadores.-.-.-.\n")
    for x in listita:
        if x[2]=="luchador":
            print(x)  
    print(".-.-.-Titan.-.-.-.\n")
    for x in listita:
        if x[2]=="titan":
            print(x)      

def promedio(listita):
    cantidad=len(listita)
    acumulador_ki=0
    for x in listita:
        acumulador_ki=acumulador_ki+x[1]
    prom=acumulador_ki/cantidad
    return prom

def maximo(listita):
    mayor=0
    for x in listita:
        if x[1]>=mayor:
            mayor=x[1]
    return mayor

def minimo(listita):
    menor=100000
    for x in listita:
        if x[1<=menor]:
            menor=x[1]
    return menor



estado_ki=False
while True:    
    print(".-.-.-. M E N U .-.-.-.-\n")
    print("1.- Asignar nivel de ki")
    print("2.- Imprimir y ordenar luchadores")
    print("3.- Estadisticas")
    print("4.- Generar BBDD")
    print("5.- Llamar al gran patriarca")
    print("0.- Salir\n")
    op = int(input("Ingrese una opción : "))
    if op == 1:
        print("")
        if estado_ki==False:
            for x in lista:
                ki = asignar_ki()
                categoria=asigna_categoria(ki)
                x.append(ki)
                x.append(categoria)
                #x.extend([ki,categoria])
            estado_ki=True
        else:
            print("El ki de los luchadores ya se ha asignado...")
            print("")
    elif op == 2:
        print("")
        imprimir(lista)

    elif op == 3:
        print("")
        ki_promedio=promedio(lista)
        ki_mayor=maximo(lista)
        ki_menor=minimo(lista)
        print(f"El ki promedio de los luchadores es {ki_promedio}")
        print(f"El ki máximo de los luchadores es {ki_mayor}")
        print(f"El ki mínimo de los luchadores es {ki_menor}")

    elif op == 4:
        print("")
        print(".-.-.-Generando base de datos.-.--.")
        print("")
        with open('luchadores.csv','w', newline='') as luchadores:
            escritor_csv=csv.writer(luchadores)
            escritor_csv.writerow(['nombre','ki','categoría'])
            escritor_csv.writerows(lista)
        print("El archivo se generó correctamente...")

    elif op == 5:
        print(".-.-.-Llamar al gran aptriarca.--.--")
        for x in lista:
            ki_aumentado=x[1]*1.25
            x.append(ki_aumentado)
        print("")
        print("El ki de los luchadores se aumentó correctamente...")
        print("")
    elif op == 0:
        print("adios...")
        break
    else:
        print("")
        print("Error!! Ingrese una opción válida...")
        print("")