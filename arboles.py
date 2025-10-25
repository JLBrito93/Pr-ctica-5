class Arbol:
    """Clase para representar árboles binarios recursivos. La variable 'raiz'
    es un elemento, 'izquierdo' es un árbol y 'derecho' es un árbol.
    """
    def __init__(self, raiz=None, izquierdo=None, derecho=None):
        """Constructor de la clase. Si raiz es None construye un árbol binario
        vacío, en otro caso, asigna a raiz como raíz del árbol, a izquierdo
        como subárbol izquierdo, y a derecho como subárbol derecho.
        """
        if raiz is None:
            self.raiz = self.izquierdo = self.derecho = None
        else:
            self.raiz = raiz
            if izquierdo is None:
                self.izquierdo = Arbol()
            elif not isinstance(izquierdo, Arbol):
                raise TypeError("¡El subárbol izquierdo debe ser árbol!")
            else:
                self.izquierdo = izquierdo
            if derecho is None:
                self.derecho = Arbol()
            elif not isinstance(derecho, Arbol):
                    raise TypeError("¡El subárbol derecho debe ser árbol!")
            else:
                self.derecho = derecho


    def __eq__(self, arbol):
        """Compara dos árboles binarios y devuelve True si son iguales,
        False en otro caso."""
        return (self.raiz == arbol.raiz
                and self.izquierdo == arbol.izquierdo
                and self.derecho == arbol.derecho)


    def __repr__(self):
        """Representación en cadena, legible para humanos, de
        un árbol. Ejemplo:
        (10,
        (5
        (1
        ø
        ø)
        (6
        ø
        ø)))
        """
        # def contador_derecho(self, prof):
        #     # return f"({self.raiz}\n{profundidad(prof+1)}{self.derecho}\n{profundidad(prof+1)}{self.izquierdo})"
        #     if self is None:
        #         return prof
        #     prof += 1
        #     return contador_derecho(self.derecho, prof)
        #
        # def contador_izquierdo(self, prof):
        #     if self is None:
        #         return prof
        #     prof += 1
        #     return contador_izquierdo(self.izquierdo, prof)
        #
        #     return prof
        #
        #
        #
        # #hola hola
        #
        # if self == Arbol():
        #     return "ø"
        # #aquí poner profundidad valor
        # return f"({self.raiz}\n{" "*contador_izquierdo(self,-2)}{self.izquierdo}\n{" "*contador_derecho(self,-2)}{self.derecho})"
        # #nivel = profundidad(2)
        # #profundidad = 0 // "  "*2
        #
        # return "("+str(self.raiz) +"\n"+ profundidad(2) + repr(self.derecho) +"\n" + profundidad(2) + repr(self.izquierdo) + ")"

    #Se comentó en la tarea que esta no sería recursiva.
    #Al no pedir más que True si es vacío, notamos que de serlo su raíz en el más alto nivel es None, de modo que
    #solo es necesario un chequeo. Si es el caso, el árbol es necesariamente vacío. En cualquier otro caso
    #regresa False
    def es_vacio(self):
        """Devuelve True si el árbol es vacío, y False en otro caso."""
        if self.raiz is None:
            return True
        return False

    #También se comentó que esta no sería recursiva en la asignación. Nuevamente consideramos que es así ya que
    #solo es necesario un chequeo para poder determinar si un árbol consiste en una sola hoja (un nodo). Así,
    #es_hoja checa si la raíz de un árbol no es None, en cuyo caso tiene raíz. Entonces solo checa si sus hijos
    #son vacíos, y solo si ambos lo son devuelve True. En otro caso es un árbol vacío y regresa False al no ser
    #una hoja.
    def es_hoja(self):
        """Devuelve True si el árbol tiene un único nodo, y False en otro caso.
        """
        if self.raiz is not None:
            if self.derecho == Arbol() and self.izquierdo == Arbol():
                return True
            else:
                return False
        return False


    def copia(self):
        """Devuelve un nuevo árbol idéntico a este."""
        return Arbol()

    #La función es tal que suma 1 por la raíz del árbol y luego cuenta recursivamente los nodos al aplicarse a
    #los subárboles. De este modo en la recursión se suman todas las raíces (nodos) que se encuentran en los hijos
    #de las raíces superiores.
    def num_nodos(self):
        """Devuelve el número de nodos en el árbol."""
        if self.raiz is None:
            return 0
        return 1+ self.derecho.num_nodos() + self.izquierdo.num_nodos()


    def direccion(self, elemento):
        """Si elemento se encuentra en el árbol, devuelve cadena con la
        dirección (en binario) del primer nodo del árbol (en un recorrido
        in-order) que contenga al elemento.   En otro caso devuelve False.
        """
        #Esto no sirve jajaj
        # if self.raiz == elemento:
        #     return "ok"
        # ruta = ""
        # if self.derecho == elemento:
        #     ruta = ruta +"0"
        # if self.izquierdo == elemento:
        #     ruta = ruta +"1"
        # return ruta


    def gira(self, direccion):
        """Recibe como entrada una dirección dada como una cadena binaria, y gira
        (intercambia el subárbol izquierdo por el derecho) el subárbol que tiene
        como raíz al nodo con la dirección dada.  El árbol original no es
        alterado, se devuelve una copia del árbol girado.   Si la dirección no
        corresponde a un nodo del árbol, se devuelve una copia del árbol
        original.
        """
        return Arbol()


    def es_isomorfo(self, arbol):
        """Compara dos árboles binarios y devuelve True si son isomorfos,
        False en otro caso.
        """
        return False

if __name__ == "__main__":
    t1=Arbol(3)
    t2=Arbol(1,t1,t1)
    t3=Arbol()
    t4=Arbol(2,t3,t2)
    #b=Arbol(c,Arbol(),Arbol(d))
    #print(t4.es_vacio())
    print(t4.direccion(2))