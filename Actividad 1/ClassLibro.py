from ClassCapitulo import Capitulo

class Libro:

    __idLibro = 0
    __titulo = ''
    __autor = ''
    __editorial = ''
    __isbn = 0
    __cantCapitulos = ''
    __capitulos = None

    def __init__(self, idLibro, titulo, autor, editorial, isbn, cantcapitulos):
        self.__idLibro = idLibro
        self.__titulo = titulo
        self.__autor = autor
        self.__editorial = editorial
        self.__isbn = isbn
        self.__cantCapitulos = cantcapitulos
        self.__capitulos = []

    def mostrarLibros(self):
        print("\nId: {}\nTitulo: {}\nEditorial: {}\nIsbn: {}\nCantidad de capitulos: {}".format(self.__idLibro,self.__titulo,self.__editorial,self.__isbn,self.__cantCapitulos))
        if(self.__cantCapitulos == (len(self.__capitulos))):
            for c in self.__capitulos:
                print("---------------")
                c.mostrarCapitulo()

    def agregarCapitulo(self,titulocapitulo,cantpaginas):
        self.__capitulos.append(Capitulo(titulocapitulo,cantpaginas))

    def getIdLibro(self):
        return self.__idLibro

    def getTitulo(self):
        return self.__titulo

    def getAutor(self):
        return self.__autor

    def getEditorial(self):
        return self.__editorial

    def getCapitulos(self):
        return self.__capitulos
