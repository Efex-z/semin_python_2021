import unittest
from Pila import Pila


class TestPila(unittest.TestCase):
    def test_case1(self):
        """ Testea que el metodo cantidad de la pila devuelva la cantidad correcta de elementos
        aunque sean de distinto tipo, creando una pila vacia al comienzo """
        p = Pila()
        p.apilar("uno")
        p.apilar(2)
        self.assertEqual(p.cantidad(), 2)

    def test_case2(self):
        """ Testea que el metodo cantidad de la pila devuelva una cantidad correcta si se agrega
        un elemento solo en la inicializacion de la pila """
        p = Pila(["elemento"])
        # no se qué es más correcto: si usar assertEqual o usar assertTrue.
        # asumo que el True es que apunten al mismo elemento, mientras que el Equal compara valores.
        # en este caso, como son enteros, apuntarían al mismo "1"
        self.assertTrue(p.cantidad() == 1)

    def test_case3(self):
        """ Testea que el método __str__ devuelva un string con la pila en orden desde el tope
        hacia el fondo correctamente"""
        p = Pila("caracteres")
        cadena = p.__str__()
        comparar = "Los elementos de la pila (de tope a fondo) son:\n s e r e t c a r a c"
        self.assertEqual(cadena, comparar)
        comparar2 = "Los elementos de la pila (de tope a fondo) son:\n s e r e t c a r a"
        self.assertNotEquals(cadena, comparar2)

    def test_case4(self):
        """ Testea que se agreguen correctamente los elementos a una pila """
        p = Pila([1, "dos", {"tres": 3}, [4, "cuatro"], (5, "cinco")])
        # el assertEqual espera un elemento de ti
        self.assertEqual(p.valores, [1, "dos", {"tres": 3}, [4, "cuatro"], (5, "cinco")])
        # no sé cuál de las dos opciones es más pythonic
        self.assertListEqual(p.valores, [1, "dos", {"tres": 3}, [4, "cuatro"], (5, "cinco")])


if __name__ == '__main__':
    unittest.main()
