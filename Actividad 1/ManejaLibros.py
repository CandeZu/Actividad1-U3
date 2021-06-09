import csv
from ClassLibro import Libro
from ClassCapitulo import Capitulo
import re

class ManejadorLibros:
    __listaLibros = None

    def __init__(self):
        self.__listaLibros = []

    def agregarLibro(self, unLibro):
        self.__listaLibros.append(unLibro)

    def testLibros(self):
        archivo = open('libros.csv')
        reader = csv.reader(archivo, delimiter=',')
        bandera = True
        for fila in reader:
                if len(fila)==6:
                    idLibro=int(fila[0])
                    titulo=fila[1]
                    autor=fila[2]
                    editorial=fila[3]
                    isbn=int(fila[4])
                    cantCapitulos=int(fila[5])
                    unLibro=Libro(idLibro,titulo,autor,editorial,isbn,cantCapitulos)
                    self.agregarLibro(unLibro)
                else:
                    tituloCapitulo=fila[0]
                    cantPaginas=int(fila[1])
                    unLibro.agregarCapitulo(tituloCapitulo,int(cantPaginas))
        archivo.close()
    
    def mostrarLista(self):
        for libro in self.__listaLibros:
            print("---------------------------------------------------")
            libro.mostrarLibros()
    
    def buscarLibro(self, identificador):
        i=0
        acu=0
        band=False
        while ((i<(len(self.__listaLibros))) and band==False):
            if (identificador==self.__listaLibros[i].getIdLibro()):
                band=True
                print("\nTitulo del libro: {}".format(self.__listaLibros[i].getTitulo()))
                for capitulo in self.__listaLibros[i].getCapitulos():
                    
                    capitulo.mostrarCapitulo()
                    acu=capitulo.totalPaginas(acu)
            i+=1
        
        print("Total de páginas: {}".format(acu))
        

    def buscarPalabra(self, palabra):
        for libro in self.__listaLibros:
            if re.search(palabra,libro.getTitulo()):
                print("Coincide en el libro: ")
                print("Titulo: {}\nAutor: {}".format(libro.getTitulo(),libro.getAutor()))
            
            for capitulo in libro.getCapitulos():
                if re.search(palabra,capitulo.getTituloCap()):
                    print("Coincide en el capitulo: ")
                    print("Titulo del libro: {}\nAutor: {}\nCapitulo: {}".format(libro.getTitulo(),libro.getAutor(),capitulo.getTituloCap()))

    