lista=[1,"Elias Vicencio",3]
print (lista)
##
print (lista[1])
for x in lista:
    print("---------------------------------------------")
    print (x)

##Funciones:
print("\n"*2)
##agregar elementos .append()
lista.append("Emma Stone")
for x in lista:
print("---------------------------------------------")
print(x)

##insertar elementos .insert(pos,elementos)
print("---------------------------------------------")
lista.insert(1,"megan fox")
for x in lista:
    print(x) 
##borrar elementos .remove(elemento)
lista.remove("Emily Blunt") 
print("---------------------------------------------")
for x in lista:
    print(x)


elemento="megan fox"
for x in lista:
    if x==elemento:
        encontrado=True
        break

    if elemento in lista: