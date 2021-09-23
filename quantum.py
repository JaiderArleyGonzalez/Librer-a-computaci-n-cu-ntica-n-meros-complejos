from math import sqrt
from matplotlib import pyplot
import numeroscomplejos as lc
import random
def Experiment_Marbles(A, V, t):
    """Función que simula los clicks para el experimento 
    de la canicas con coeficientes booleanos.
    (list),(list),(int) → (list)"""
    vector = V
    index = 0
    while index < t:
        vector_click = lc.AccionMatVec(A, vector)
        vector = vector_click
        index += 1
    return vector
def ExperimentSlitsMatriz(matriz_adyacencia):
    """Función que simula el experimento de las múltiples 
    rendijas clásico probabilístico, con más de dos rendijas.
    Generador de la matriz resultante
    (list) → (list)"""
    b2 = lc.ProductMatrix(matriz_adyacencia, matriz_adyacencia)
    return b2
def ExperimentSlitsVector(b2, state):
    """Función que simula el experimento de las múltiples 
    rendijas clásico probabilístico, con más de dos rendijas.
    Generador del vector
    (list),(list) → (list)"""
    vector_click = lc.AccionMatVec(b2, state)
    return vector_click
def random_color():
    color = ["#"+''.join([random.choice('0123456789ABCDEF') for j in range(6)])]
    return color
def graficador(vector_estados):
    """Función que grafica con un diagrama de barras las probabilidades de un vector de estados.
     Guardar el gráfico en el computador con un formato png"""
    vertices = []
    colores = []
    for i in range(1, len(vector_estados) + 1):
        vertices += [i]
        colores += [random_color()]
    pyplot.title("probabilidades de un vector de estados")
    pyplot.bar(vertices, height = vector_estados, color = colores, width = 0.5)
    pyplot.ylabel("probabilidad")
    pyplot.savefig("probabilidades.png")
    pyplot.show()



