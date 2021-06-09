class Capitulo:
    __titulo = ''
    __cantPaginas = 0

    def __init__(self, titulo, cantPaginas):
        self.__titulo = titulo
        self.__cantPaginas = cantPaginas
    
    def getTituloCap(self):
        return self.__titulo

    def getPaginas(self):
        return self.__cantPaginas

    def mostrarCapitulo(self):
        print("\nCapitulo: {}\nCantidad de Paginas: {}".format(self.__titulo, self.__cantPaginas))
    
    def totalPaginas(self, acum):
        acum+=self.__cantPaginas
        return acum
