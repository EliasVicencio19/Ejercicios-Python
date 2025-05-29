##Realizar un  menú para operaciones matematicas, donde se pueda 
# sumar, restar, multiplicar y dividir y esto lance un resultado.

def menu():
    while True:
        print("1.- Sumar")
        print("2.- Restar")
        print("3.- Multiplicar")
        print("4.- Dividir")
        print("0.- Salir\n")

        try:
            opc = int(input("Ingrese una opción: "))
        except ValueError:
            print("Error: Ingrese una opción válida.")
            continue

        if opc in (1, 2, 3, 4):
            try:
                num1 = float(input("Ingrese el primer número: "))
                num2 = float(input("Ingrese el segundo número: "))
            except ValueError:
                print("Error 1615: Ingrese números válidos.")
                continue

        if opc == 1:
            print(f"Resultado: {num1 + num2}")

        elif opc == 2:
            print(f"Resultado: {num1 - num2}")

        elif opc == 3:
            print(f"Resultado: {num1 * num2}")

        elif opc == 4:
            try:
                print(f"Resultado: {num1 / num2}")
            
            except ZeroDivisionError:
                print("Error 1904: No se puede dividir por cero.")

        elif opc == 0:
            print("Saliendo del programa...")
            break

menu()