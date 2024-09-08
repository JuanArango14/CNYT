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
escalar = int (input('Digite el numero escalar por el cual quiere multiplicar: ')) # Defining scalars
def multi_vector_escalar(vector1, escalar):
    return vector1 * escalar

#Addition of complex matrix
matriz1 = np.array([z1, z2],[z3, z4]) # Defining Matrix
matriz2 = np.array([z3, z4], [z1,z2]) # Defining Matrix
def Addition_matrix (matriz1,matriz2):
    return  matriz1 + matriz2

#Inverse of Matrix
def Inverse_matrix (matriz1):
    return np.linalg.inv(matriz1)

#CALCULATIONS:
result_addition = sum_vectores(vector1, vector2)
inverse_vector1 = inverseV(vector1)
result_multiplyes = multi_vector_escalar(vector1, escalar)
result_additionMTX = Addition_matrix (matriz1, matriz2)
result_inverse_matrix = Inverse_matrix
def main():
    print("Resultado de la adición de vectores complejos:", result_addition)
    print("Inverso aditivo del vector complejo:", inverse_vector1)
    print("Resultado de la multiplicación de un escalar por un vector de complejos:", result_multiplyes)
    print("Resultado de la suma de matrices complejas:", result_additionMTX)
    print("Resultado de el inverso de una matriz de complejos:", result_inverse_matrix)
()










# Conjugate and absolute value or modulus
print("Conjugate of (3 -4j):", c7.conjugate())
print("Absolute value of (3 -4j):", abs(c7))
