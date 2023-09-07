import numpy as np
import math


def sumar_vectores(vector1, vector2):
    """Calcula la suma de dos vectores complejos."""
    suma = np.add(vector1, vector2)
    return suma


def inverso_vector(vector):
    """ Calcula el inverso aditivo de un vector complejo."""
    inverso = np.negative(vector)
    return inverso


def mult_escalar_vector(escalar, vector):
    """Calcula la multiplicación de un escalar por un vector complejo."""
    multiplicacion = np.multiply(escalar, vector)
    return multiplicacion


def sumar_matrices_complejas(matriz_1, matriz_2):
    """ Realiza la suma de dos matrices complejas."""
    suma_matrices = np.add(matriz_1, matriz_2)
    return suma_matrices


def inversa_matriz(matriz):
    """ Calcula la inversa aditiva de una matriz compleja."""
    inversa_mat = np.negative(matriz)
    return inversa_mat


def mult_escalar_matriz(escalar, matriz):
    """Realiza la multiplicación de un escalar por una matriz compleja."""
    mult_escalar_mat = np.multiply(escalar, matriz)
    return mult_escalar_mat


def matriz_transpuesta(matriz):
    """ Calcula la transpuesta de una matriz o vector complejo."""
    transpuesta = np.transpose(matriz)
    return transpuesta


def matriz_conjugada(matriz):
    """ Calcula la matriz conjugada de una matriz o vector complejo."""
    conjugada = np.conjugate(matriz)
    return conjugada


def adjunta(matriz):
    """Calcula la adjunta (daga) de una matriz o vector"""
    adjunta = matriz_transpuesta(matriz_conjugada(matriz))
    return adjunta


def producto_matrices(mat1, mat2):
    """Calcula el producto entre 2 matrices (de tamaños compatibles)"""
    m1 = len(mat1)
    n1 = len(mat1[0])
    m2 = len(mat2)
    n2 = len(mat2[0])
    if n1 != m2:
        return "No son matrices compatibles"
    else:
        matriz = [[0 for row in range(n2)] for col in range(m1)]
        for i in range(m1):
            for j in range(n2):
                for k in range(m2):
                    matriz[i][j] += mat1[i][k] * mat2[k][j]
        return matriz


def accion(matriz, vector):
    """Calcula la "acción" de una matriz sobre un vector."""
    matriz = np.array(matriz)
    vector = np.array(vector)
    rest = np.dot(matriz, vector)
    return str(rest)


def producto_interno(vector_1, vector_2):
    """Calcula el Producto interno de dos vectores"""
    suma = 0
    for i in range(len(vector_1)):
        suma += vector_1[i] * vector_2[i]
    return suma


def norma_vector(vector):
    """Calcula la norma de un vector."""
    suma = 0
    for i in range(len(vector)):
        suma += abs(vector[i]) ** 2
        print(suma)
    return round((suma) ** 0.5, 2)


def distancia_vectores(vector1, vector2):
    """Calcula la distancia entre dos vectores."""
    suma_cuadrados = 0
    for i in range(len(vector1)):
        diferencia = vector1[i] - vector2[i]
        suma_cuadrados += diferencia ** 2
    distancia = math.sqrt(suma_cuadrados)
    return distancia


def valor_vector_propio(matriz):
    """Calcula los valores  y vectores propios de una matriz."""
    valores_propios = np.linalg.eig(matriz)
    vectores_propios = np.linalg.eig(matriz)
    return valores_propios, vectores_propios


def producto_tensor_matriz(A, B):
    m = len(A)
    n = len(B)
    m1 = len(A[0])
    n1 = len(B[0])
    fila = m * n
    columna  = m1 * n1
    resultado = [[0 for fil in range (fila)] for colum in range (columna)]
    for j in range (fila):
        for k in range (columna):
            resultado[j][k] = (A[j//n][k//n1]*B[j%n][k%n1])
    return resultado


if __name__ == '__main__':
    """Estos print se utilizan para probar el correcto funcionamiento de cada función
    (Herramienta del programador)"""
    # Casos de prueba para las funciones de operaciones con números complejos
    """Para hacer correcto uso de esta librería se debe tener en cuenta que 
     los números complejos se van a representar con j."""
    # Vectores complejos
    vec1 = [1 + 2j, 3 - 1j]
    vec2 = [2 - 1j, 4 + 3j]

    # Matrices complejas
    mat1 = [[1 + 2j, 3 - 1j], [0 + 1j, -2 - 3j]]
    mat2 = [[2 - 1j, 4 + 3j], [1 - 2j, 5 + 4j]]
    mat3 = [[1 + 2j, 3 - 1j], [0 + 1j, -2 - 3j]]

    A = [[1, 2], [2, 1]]
    B = [[4, 5,], [5, 4]]
    # Pruebas para las funciones de operaciones con números complejos
    print("Suma de vectores complejos:", sumar_vectores(vec1, vec2))
    print("Inverso de vector complejo:", inverso_vector(vec1))
    print("Multiplicación escalar de vector complejo:", mult_escalar_vector(2 + 3j, vec1))

    print("Suma de matrices complejas:\n", sumar_matrices_complejas(mat1, mat2))
    print("Inversa de matriz compleja:\n", inversa_matriz(mat1))
    print("Multiplicación escalar de matriz compleja:\n", mult_escalar_matriz(2 - 1j, mat2))

    print("Matriz transpuesta:\n", matriz_transpuesta(mat3))
    print("Matriz conjugada:\n", matriz_conjugada(mat3))

    print("----------------------------------Prueba ult def------------------------------")
    print(A)
    print(B)
    print("El prodcuto tensor de 2 matrices es:",  producto_tensor_matriz(A, B))


    print("--------------------Prueba ")
