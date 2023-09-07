import Operaciones_cplx as oper
import unittest
import numpy as np
"""-------------------Archivo con pruebas automáticas de las funciones-------------------"""

class TestLibVecSpace(unittest.TestCase):

    def test_suma_vec(self):
        """Prueba 1: Adición de vectores complejos"""
        c1 = [2 + 6j, -4 - 9j]
        c2 = [2 + 6j, 5 + 17j]
        sum_ver = [(4 + 12j), (1 + 8j)]
        sum_doc = oper.sumar_vectores(c1, c2)
        self.assertEqual(sum_doc, sum_ver)

    def test_inverso(self):
        """Prueba 2: Inverso (aditivo) de un vector complejo."""
        c1 = [8.9 + 4.8j, 2.9 - 8.4j]
        sum_ver = [(-8.9 - 4.8j), (-2.9 + 8.4j)]
        sum_doc = oper.inverso_vector(c1)
        self.assertEqual(sum_doc, sum_ver)

    def test_mult(self):
        """Prueba 3: Multiplicación de un escalar por un vector complejo."""
        c1 = [8.9 + 4.8j, 2.9 - 8.4j]
        esc = 5
        sum_ver = [(44.5 + 24j), (14.5 - 42j)]
        sum_doc = oper.mult_escalar_vector(esc, c1)
        self.assertEqual(sum_doc, sum_ver)

    def test_suma_matrix(self):
        """Prueba 4: Adición de matrices complejas."""
        mat1 = [[1 + 4j, -1 - 12j, 4 + 7j], [-4 + 2j, 45 - 1j, 13 + 7j], [2 + 14j, 2 + 9j, 1 + 3j]]
        mat2 = [[1 + 4j, -1 - 12j, 4 + 7j], [-4 + 2j, 45 - 1j, 13 + 7j], [2 + 14j, 2 + 9j, 1 + 3j]]
        sum_ver = [[(2 + 8j), (-2 - 24j), (8 + 14j)], [(-8 + 4j), (90 - 2j), (26 + 14j)],
                   [(4 + 28j), (4 + 18j), (2 + 6j)]]
        sum_doc = oper.sumar_matrices_complejas(mat1, mat2)
        self.assertEqual(sum_doc, sum_ver)

    def test_inversa(self):
        """Prueba 5 :Inversa (aditiva) de una matriz compleja."""
        mat1 = [[1 + 4j, -1 - 12j, 4 + 7j], [-4 + 2j, 45 - 1j, 13 + 7j], [2 + 14j, 2 + 9j, 1 + 3j]]
        sum_ver = [[(-1 - 4j), (1 + 12j), (-4 - 7j)], [(4 - 2j), (-45 + 1j), (-13 - 7j)],
                   [(-2 - 14j), (-2 - 9j), (-1 - 3j)]]
        sum_doc = oper.inversa_matriz(mat1)
        self.assertEqual(sum_doc, sum_ver)

    def test_mult_esc(self):
        """Prueba 6: Multiplicación de un escalar por una matriz compleja."""
        mat1 = [[1 + 4j, -1 - 12j, 4 + 7j], [-4 + 2j, 45 - 1j, 13 + 7j], [2 + 14j, 2 + 9j, 1 + 3j]]
        escalar = 5
        sum_ver = [[(5 + 20j), (-5 - 60j), (20 + 35j)], [(-20 + 10j), (225 - 5j), (65 + 35j)],
                   [(10 + 70j), (10 + 45j), (5 + 15j)]]
        sum_doc = oper.mult_escalar_matriz(escalar, mat1)
        self.assertEqual(sum_doc, sum_ver)

    def test_mat_transpuesta(self):
        """Prueba 7: Transpuesta de una matriz/vector."""
        mat = [[1 + 4j, -1 - 12j, 4 + 7j], [-4 + 2j, 45 - 1j, 13 + 7j], [2 + 14j, 2 + 9j, 1 + 3j]]
        sum_ver = [[(1 + 4j), (-4 + 2j), (2 + 14j)], [(-1 - 12j), (45 - 1j), (2 + 9j)], [(4 + 7j), (13 + 7j), (1 + 3j)]]
        sum_doc = oper.matriz_transpuesta(mat)
        self.assertEqual(sum_doc, sum_ver)

    def test_conjugada(self):
        """Prueba 8: Conjugada de una matriz/vector"""
        mat1 = [[1 + 4j, -1 - 12j, 4 + 7j], [-4 + 2j, 45 - 1j, 13 + 7j], [2 + 14j, 2 + 9j, 1 + 3j]]
        sum_ver = [[(1 - 4j), (-1 + 12j), (4 - 7j)], [(-4 - 2j), (45 + 1j), (13 - 7j)], [(2 - 14j), (2 - 9j), (1 - 3j)]]
        sum_doc = oper.matriz_conjugada(mat1)
        self.assertEqual(sum_doc, sum_ver)

    def test_adjunta(self):
        """Prueba 9: Adjunta (daga) de una matriz/vector"""
        mat1 = [[1 + 4j, -1 - 12j, 4 + 7j], [-4 + 2j, 45 - 1j, 13 + 7j], [2 + 14j, 2 + 9j, 1 + 3j]]
        sum_ver = [[(1 - 4j), (-4 - 2j), (2 - 14j)], [(-1 + 12j), (45 + 1j), (2 - 9j)], [(4 - 7j), (13 - 7j), (1 - 3j)]]
        sum_doc = oper.adjunta(mat1)
        self.assertEqual(sum_doc, sum_ver)

    def test_product_mat(self):
        """Prueba 10: Producto de dos matrices (de tamaños compatibles)"""
        mat1 = [[1 + 4j, -1 - 12j, 4 + 7j], [-4 + 2j, 45 - 1j, 13 + 7j], [2 + 14j, 2 + 9j, 1 + 3j]]
        mat2 = [[1 + 4j, -1 - 12j, 4 + 7j], [-4 + 2j, 45 - 1j, 13 + 7j], [2 + 14j, 2 + 9j, 1 + 3j]]
        sum_ver = [[(-77 + 124j), (-65 - 505j), (30 - 121j)], [(-262 + 276j), (2015 + 87j), (554 + 328j)],
                   [(-120 + 10j), (240 + 380j), (-135 + 207j)]]
        sum_doc = oper.producto_matrices(mat1, mat2)
        self.assertEqual(sum_doc, sum_ver)

    def test_accion(self):
        """Prueba 11: Función para calcular la "acción" de una matriz sobre un vector."""
        matriz = [[2 + 4j, 3 - 2j], [4 - 8j, 5 + 1j]]
        vector = [1 + 6j, 2 - 9j]
        sum_ver = "[-34.-15.j  71.-27.j]"
        sum_doc = oper.accion(matriz, vector)
        self.assertEqual(sum_doc, sum_ver)

    def test_producto_int(self):
        """Prueba 12: Producto interno de dos vectores."""
        c1 = [1 + 5j, -4 - 9j]
        c2 = [1 + 5j, 5 + 17j]
        resp_verd = (109 - 103j)
        resp_doct = oper.producto_interno(c1,c2)
        self.assertEqual(resp_doct, resp_verd)

    def test_norma_vec(self):
        """Prueba 13: Norma de un vector."""
        c1 = [1 + 5j, -4 - 9j]
        resp_verd = 11.09
        resp_doct = oper.norma_vector(c1)
        self.assertEqual(resp_doct, resp_verd)

    def test_distance_vect(self):
        """Prueba 14: Distancia entre dos vectores."""
        vector1 = [7 + 3j]
        vector2 = [1 - 5j]
        resp_verd = 10.0
        resp_doct = oper.distancia_vectores(vector1, vector2)
        self.assertEqual(resp_doct, resp_verd)

    def test_val_vec_prop(self):
        """Prueba 15. Valores  y vectores propios de una matriz."""
        matriz = [[1, 2, -1], [1, 0, 1],[4, -4, 5]]
        resp_verd = """los valores propios para esta matriz o vector son [3. 2. 1.] y 
        los vectores son [[-0.23570226  0.43643578  0.40824829]
        [ 0.23570226 -0.21821789 -0.40824829]
        [ 0.94280904 -0.87287156 -0.81649658]]"""
        resp_doct = oper.valor_vector_propio(matriz)
        self.assertEqual(resp_doct,resp_verd)

if __name__ == '__main__':
    unittest.main()
