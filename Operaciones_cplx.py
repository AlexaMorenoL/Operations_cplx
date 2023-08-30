import numpy as np

def sumar_vectores(vector1, vector2):
    """Calcula la suma de dos vectores complejos.
    Se deben ingresar 2 vectores complejos v1 y v2.
    Esta función retorna el resultado de la adición de los vectores complejos."""
    suma = np.add(vector1, vector2)
    return suma

def inverso_vector(vector):
    """ Calcula el inverso aditivo de un vector complejo.
    Se debe ingresar el vector complejo y se retorna el inverso."""
    inverso = np.negative(vector)
    return inverso

def mult_escalar_vector(escalar, vector):
    """Calcula la multiplicación de un escalar por un vector complejo.
    Se debe ingresar el escalar y el vector para que la función retorne el resultado."""
    multiplicacion =np.multiply(escalar, vector)
    return multiplicacion

def sumar_matrices_complejas(matriz_1, matriz_2):
    """ Realiza la suma de dos matrices complejas.
    Se ingresan 2 matrices y se devuelve el resultado de la suma."""
    suma_matrices = np.add(matriz_1, matriz_2)
    return suma_matrices

def inversa_matriz(matriz):
    """ Calcula la inversa aditiva de una matriz compleja.
    Se debe ingresar la matriz  compleja y se retorna la inversa."""
    inversa_mat = np.negative(matriz)
    return inversa_mat

def mult_escalar_matriz(escalar, matriz):
    """Realiza la multiplicación de un escalar por una matriz compleja.
    Se debe ingresar el escalar y la matriz para que la función retorne el resultado."""
    mult_escalar_mat = np.multiply(escalar, matriz)
    return mult_escalar_mat

def matriz_transpuesta(matriz):
    """ Calcula la transpuesta de una matriz o vector complejo.
    Recibe una matriz o vector y retorna la traspuesta del mismo."""
    transpuesta = np.transpose(matriz)
    return transpuesta
def matriz_conjugada(matriz):
    """ Calcula la matriz conjugada de una matriz o vector complejo.
    Recibe una matriz o vector complejo y retorna la matriz o vector conjugado."""
    conjugada = np.conjugate(matriz)
    return conjugada

if __name__ == '__main__':
    """Estos print se utilizan para probar el correcto funcionamiento de cada función 
    (Herramienta del programador) """
    print("La conjugada, es: ", matriz_conjugada((2+3, -2+3, 1-2, 1+2)))