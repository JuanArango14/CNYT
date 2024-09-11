#Libreria computacion cuantica: Complex Calculator
#Juan Felipe Arango Hidalgo
#Ciencias y Tecnologia
#Escuela Colombiana de Ingenieria Julio Garavito

import cmath
import numpy as np

#   Basic operations


# Defining complex number
z1 = complex(5, 6) # 5 + 6j
z2 = complex(7, -8) # 7 -8j
z3 = complex(7, -8) # 7 -8j
z4 = complex (2. -3) # 2 -3j

vector1 = np.array([z1, z2])
vector2 = np.array([z3, z4])


# Addition of 2 complex numbers
def sum_vectores(vector1, vector2):
    return vector1 + vector2

#Inverse of vector
def inverseV(vector): 
   return -vector

#Multiplication of vector with scalar number   
escalar = 3 # Defining scalars
def multi_vector_escalar(vector1, escalar):
    return vector1 * escalar

#Addition of complex matrix
matriz1 = np.array([[z1, z2], [z3, z4]]) # Defining Matrix
matriz2 = np.array([[z3, z4], [z1, z2]]) # Defining Matrix
def Addition_matrix (matriz1,matriz2):
    return  matriz1 + matriz2

#Inverse of Matrix
def Inverse_matrix (matriz1):
    return np.linalg.inv(matriz1)

#Multiplication of matix with scalar number
def Multiply_matrix ( matriz1, escalar):
    return matriz1 * escalar

#Transpose of matrix and vector
def transpose_vector(vector1):
    return np.transpose(vector1)

def transpose_matrix(matriz1):
    return np.transpose (matriz1)

#Conjugate matrix - conjugate vector

def conjugate_matrix(matriz1):
    return np.conjugate(matriz1)

def conjugate_vector(vector1):
    return np.conjugate(vector1)

#Daga or dagger (conjugada transpuesta) matrix
def daga_matrix(matriz1):
    return np.conjugate(np.transpose(matriz1))

#Daga or dagger (conjugada transpuesta) vector
def daga_vector(vector1):
    return np.conjugate(np.transpose(vector1))

#Product of two matrix
def producto_matrices(matriz1, matriz2):
    return np.dot(matriz1, matriz2)

#Action of matrix on a vector
def action_matrices(matriz1, vector1):
    return np.dot(matriz1, vector1)

#Inner product of two vector
def inner_product(vector1, vector2):
    return np.inner(vector1, vector2)

#Norma of vector
def norma_vector(vector1):
    return np.linalg.norm(vector1)

#Distance between 2 vectors
def distancia_vector(vector1, vector2):
    return np.linalg.norm(vector1 - vector2)

#Valores y vectores propio de una matriz
def valores_propios(matriz2):
    return np.linalg.eig( matriz2)

#Verify if the matriz is unitary
def is_unitary(matriz1):
    return np.allclose(np.dot(matriz1, np.linalg.inv(matriz1)), np.eye(matriz1.shape[0]))

#Verify if the matriz is hermitian
def is_hermitian(matriz1):
    return np.allclose(matriz1, np.conjugate(np.transpose(matriz1)))

#Tensor product between two matrix
def tensor_product(matriz1, matriz2):
    return np.kron(matriz1, matriz2)

#Tensor product between two vector

def tensor_product_vector(vector1, vector2):
    return np.outer(vector1, vector2)



#CALCULATIONS:
result_addition = sum_vectores(vector1, vector2)
inverse_vector1 = inverseV(vector1)
result_multiplyes = multi_vector_escalar(vector1, escalar)
result_additionMTX = Addition_matrix (matriz1, matriz2)
result_inverse_matrix = Inverse_matrix (matriz1)
result_ecalarmatrix = Multiply_matrix (matriz1,escalar)
result_transpose_vector = transpose_vector(vector1)
result_transpose_matrix = transpose_matrix(matriz1)
rconjugate_matrix = conjugate_matrix(matriz1)
rconjugate_vector = conjugate_vector(vector1)
result_daga_matrix = daga_matrix(matriz1)
result_daga_vector = daga_vector(vector1)
result_producto_matrices = producto_matrices(matriz1, matriz2)
ractional_matrices = action_matrices(matriz1, vector1)
rinner_product= inner_product(vector1, vector2)
rnorma_vector= norma_vector(vector1)
rdistance_vector= distancia_vector(vector1, vector2)
rvalues_vector= valores_propios(matriz2)
runitary=is_unitary(matriz1)
rhermitian=is_hermitian(matriz1)
rtensor_matrix= tensor_product(matriz1, matriz2)
rtensor_vector= tensor_product_vector(vector1, vector2)

def main():
    print("Resultado de la adición de vectores complejos:", result_addition)
    print("Inverso aditivo del vector complejo:", inverse_vector1)
    print("Resultado de la multiplicación de un escalar por un vector de complejos:", result_multiplyes)
    print("Resultado de la suma de matrices complejas:", result_additionMTX)
    print("Resultado de el inverso de una matriz de complejos:", result_inverse_matrix)
    print("Resultado de de la multiplicacion de una matriz compleja por un escalar: ", result_ecalarmatrix)
    print("Resultado de de la transpuesta de un vector: ", result_transpose_vector)
    print("Resultado de de la transpuesta de una matriz: ", result_transpose_matrix)
    print("Resultado de la conjugada de una matriz: ", rconjugate_matrix)
    print("Resultado de la conjugada de un vector: ", rconjugate_vector)
    print("Resultado de la dagger de una matriz:", result_daga_matrix)
    print("Resultado de la dagger de un vector:", result_daga_vector)
    print("Resultado del producto de dos matrices:", result_producto_matrices)
    print("Resultado de la accion de la matriz sobre un vector:", ractional_matrices)
    print("Resultado de el producto interno de dos vectores:", rinner_product)
    print("Resultado de la norma de un vector:", rnorma_vector)
    print("Resultado de la distancia entre 2 vectores:", rdistance_vector)
    print("Resultado de los valores propios de una matriz: ", rvalues_vector)
    print("La matriz es unitaria?: ", runitary)
    print("La matriz es hermitiana?: ", runitary)
    print("Resultado del producto tensor entre dos matrices: ", rtensor_matrix)
    print("Resultado del producto tensor entre dos vectors: ", rtensor_vector)
main()









