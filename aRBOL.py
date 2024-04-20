
class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class Arbol:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar_recursivo(valor, self.raiz)

    def _insertar_recursivo(self, valor, nodo_actual):
        if valor < nodo_actual.valor:
            if nodo_actual.izquierda is None:
                nodo_actual.izquierda = Nodo(valor)
            else:
                self._insertar_recursivo(valor, nodo_actual.izquierda)
        elif valor > nodo_actual.valor:
            if nodo_actual.derecha is None:
                nodo_actual.derecha = Nodo(valor)
            else:
                self._insertar_recursivo(valor, nodo_actual.derecha)
        else:
            
            pass

    def obtener_raiz(self):
        return self.raiz.valor if self.raiz else None

    def contar_hojas(self):
        return self._contar_hojas_recursivo(self.raiz)

    def _contar_hojas_recursivo(self, nodo_actual):
        if nodo_actual is None:
            return 0
        if nodo_actual.izquierda is None and nodo_actual.derecha is None:
            return 1
        return self._contar_hojas_recursivo(nodo_actual.izquierda) + self._contar_hojas_recursivo(nodo_actual.derecha)

    def obtener_altura(self):
        return self._obtener_altura_recursivo(self.raiz)

    def _obtener_altura_recursivo(self, nodo_actual):
        if nodo_actual is None:
            return 0
        altura_izquierda = self._obtener_altura_recursivo(nodo_actual.izquierda)
        altura_derecha = self._obtener_altura_recursivo(nodo_actual.derecha)
        return max(altura_izquierda, altura_derecha) + 1


arbol = Arbol()
arbol.insertar(5)
arbol.insertar(3)
arbol.insertar(7)
arbol.insertar(1)
arbol.insertar(4)

print("Raíz del árbol:", arbol.obtener_raiz())  
print("Cantidad de hojas:", arbol.contar_hojas())  
print("Altura del árbol:", arbol.obtener_altura())  
