class Pila:
    """ una pila que se construye a partir de una lista. Para respetar LIFO, se agregara siempre al final de la lista
    y cuando se tome el valor de tope, se tomara siempre el ultimo valor de dicha lista """
    def __init__(self, una_lista=[]):
        """ en el inicializador, debe pasarse un objeto de tipo lista (un string, por ejemplo, agregaria cada uno
        de sus caracteres por separado, ya que se comporta como una lista de chars)"""
        self._valores = una_lista

    def __str__(self):
        cadena = "Los elementos de la pila (de tope a fondo) son:\n"
        for e in reversed(self.valores):
            cadena = cadena + " " + str(e)
        return cadena

    @property
    def valores(self):
        return self._valores

    @valores.setter
    def valores(self, una_lista):
        self._valores = una_lista

    def apilar(self, un_valor):
        """agrega un elemento al tope de la pila"""
        self.valores.append(un_valor)

    def desapilar(self):
        """quita el elemento del tope de la pila y lo devuelve"""
        # por default, el pop quita el ultimo elemento y lo devuelve
        return self.valores.pop()

    def cantidad(self):
        """retorna la cantidad de elementos que contiene la pila"""
        return len(self.valores)

    def tope(self):
        """retorna el elemento que esta en el tope de la pila (sin eliminarlo)"""
        # cantidad - 1 porque el primer elemento esta en la posicion 0.
        return self.valores[self.cantidad()-1]
