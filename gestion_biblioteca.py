"""SISTEMA DE GESTION DE BIBLIOTECA 
Crea un sistema de gestión de una biblioteca utilizando clases en Python. 
Debes implementar las siguientes clases:

1. “Libro”: Representa un libro con atributos como 
-título, 
-autor  
-número de ejemplares disponibles.

2. “Usuario”: Representa a un usuario de la biblioteca con atributos como 
-nombre, 
-número de identificación 
-lista de libros prestados.

3. “Biblioteca”: Representa la biblioteca en sí, con métodos para 
-agregar libros, 
-prestar libros a usuarios,
-devolver libros y 
-mostrar el inventario"""

class Libro :
    def __init__(self, titulo, autor, ejemplares_disponibles):
        self.titulo = titulo
        self.autor = autor
        self.ejemplares_disponibles = ejemplares_disponibles

class Usuario :
    def __init__(self, nombre, num_id):
        self.nombre = nombre
        self.num_id = num_id
        self.libros_prestados = []

class Biblioteca :
    def __init__(self):
        self.libros = []
    
    def agregar_libros (self,libro):
        self.libros.append(libro)


    def prestar_libro (self, usuario, titulo):
        for libro in self.libros:
            if libro.titulo == titulo and libro.ejemplares_disponibles > 0:
                usuario.libros_prestados.append (libro)
                libro.ejemplares_disponibles -= 1
                print (f"El libro {titulo} ha sido prestado a {usuario.nombre}")

                return
            
        print ("El ejemplar no esta disponible")

    def devolver_libro (self, usuario, titulo):
        for libro in usuario.libros_prestados:
            if libro.titulo == titulo:
                usuario.libros_prestados.remove(libro)
                libro.ejemplares_disponibles += 1
                print (f"El libro {titulo} ha sido devuelto por {usuario.nombre}")

    def mostrar_inventario(self):
        for libro in self.libros:
            print (f"{libro.titulo}de {libro.autor} - Disponibles: {libro.ejemplares_disponibles}")


# Ejemplo de Uso
biblioteca = Biblioteca()
libro1 = Libro ("El Gran Gatsby", "F. Scott Fitzgerald", 3)
libro2 = Libro ("Cien Años de Soledad", "Gabriel Garcia Marquez", 5)

biblioteca.agregar_libros(libro1)
biblioteca.agregar_libros(libro2)

usuario1 = Usuario("Lara", "12345")
usuario2 = Usuario ("Ana", "54321")

biblioteca.prestar_libro(usuario1, "El Gran Gatsby")
biblioteca.prestar_libro(usuario2, "Cien Años de Soledad")


biblioteca.mostrar_inventario()

biblioteca.devolver_libro(usuario1, "El Gran Gatsby")

biblioteca.mostrar_inventario()
