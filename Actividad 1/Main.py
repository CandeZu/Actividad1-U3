from ManejaLibros import ManejadorLibros
def imprimir():
    print('''---------MENU-----------
    (1) Ingresar el identificador de un libro y mostrar título del libro, nombre de cada uno de sus capítulos y cantidad total de páginas de un libro.
    (2) Dada una palabra, mostrar título y autor de los libros que contienen la palabra dada en su título o en el título de alguno de sus capítulos.
    (0) Salir.
    ------------------------''')
def menu(manejador):
    band =True
    while band:
        imprimir()
        opcion = int(input("Ingrese una opcion: "))
        if opcion == 1:
            identificador = int(input("\nIngrese identificador: "))
            manejador.buscarLibro(identificador)

        elif opcion == 2:
            palabra=input("\nIngrese palabra: ")
            manejador.buscarPalabra(palabra)

        elif opcion == 0:
            print("\nFin")
            band=False

        else:
            print("\nOpcion no valida.")

if __name__ == '__main__':
    manejador = ManejadorLibros()
    manejador.testLibros()
    print("\n-----------------LISTA DE LIBROS-------------------")
    manejador.mostrarLista()
    menu(manejador)

