import datetime

class Libro:
    def __init__(self, titulo, autor, añoPublicacion):
        self.titulo = titulo
        self.autor = autor
        self.añoPublicacion = añoPublicacion
        self.disponible = True

    def prestar(self):
        if self.disponible:
            self.disponible = False
            return f"Libro '{self.titulo}' prestado" ##Se le presta a quien lo pide.
        else:
            return "El libro no está disponible."
        
    def devolver(self):
        if self.disponible:
            self.disponible = True
            return f"Libro '{self.titulo}' devuelto"
        
    def __str__(self):
        return f"Título: {self.titulo}, Autor: {self.autor}, Año: {self.añoPublicacion}, Disponible: {'Si' if self.disponible else 'No'}"
    
class Biblioteca:
    def __init__(self, nombre):
        self.nombre = nombre
        self.libros = []

    def agregarLibro(self, libro):
        self.libros.append(libro)
        return f"Libro '{libro.titulo}' agregado"
    
    def buscarLibro(self, titulo):
        for libro in self.libros:
            if libro.titulo.lower() == titulo.lower():
                return libro
        return None
    
    def mostrarLibros(self):
        if not self.libros:
            return "No hay libros en la biblioteca"
        return "\n".join(str(Libro) for libro in self.libros)
    
    def guardarLibros(self, archivo):
        try:
            with open(archivo, 'w') as archivo:
                for libro in self.libros:
                    archivo.write(f"{libro.titulo}, {libro.autor}, {libro.añoPublicacion}, {libro.disponible}\n")
            return "Libros guardados correctamente"
        except Exception as e:
            return f"Error al guardar: {e}"
        
    def cargarLibros(self, archivo):
        try:
            with open(archivo, 'r') as archivo:
                for linea in archivo:
                    datos = linea.strip().split(',')
                    libro = Libro(datos[0], datos[1], int(datos[2]))
                    libro.disponible = datos[3] == True
                    self.libros.append(libro)
            return "Libros cargados correctamete"
        except Exception as e:
            return "Error al cargar: {e}"
        
def main():
    biblioteca = Biblioteca("Mi biblioteca")
    while True:
        print("\n   Menu   \n")
        print("1.- Agregar libro")
        print("2.- Prestar libro")
        print("3.- Devolver libro")
        print("4.- Mostrar libros")
        print("5.- Guardar libros en archivo")
        print("6.- Cargar libros desde archivo")
        print("0.- Salir\n")

        opcion = int(input("Ingrese una opción: "))

        if opcion == 1:
            titulo = input("Título: ")
            autor = input("Autor: ")
            año = input("Año de publicación: ")
            libro = Libro(titulo, autor, año)
            print(biblioteca.agregarLibro(libro))

        elif opcion == 2:
            print("")

        elif opcion == 3:
            print("")
        
        elif opcion == 4:
            print(biblioteca.mostrarLibros())

        elif opcion == 5:
            archivo = input("Nombre del archivo (ej: libros.txt): ")
            print(biblioteca.guardarLibros(archivo))

        elif opcion == 6:
            archivo = input("Nombre del archivo (ej: libros.txt): ")
            print(biblioteca.cargarLibros(archivo))

        elif opcion == 0:
            print("Saliendo del programa...")
            break

        else:
            print("Error: Ingrese una opción válida")

if __name__ == "__main__":
    main()