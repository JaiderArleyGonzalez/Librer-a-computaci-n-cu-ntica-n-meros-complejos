"""Librería Computación Cuántica: Números Complejos
Jaider Arley González Arias"""
import math
def suma_complejos(sum1, sum2):
    """Función que retorna la suma de dos números complejos
    (list) -> (list)"""
    a = sum1[0] + sum2[0]
    b = sum1[1] + sum2[1]
    suma = [a, b]
    return suma
def producto_complejos(mult1, mult2):
    """Función que retorna la multiplicación de dos números complejos
    (list) -> (list) """
    a = mult1[0] * mult2[0] - mult1[1] * mult2[1]
    b = mult1[0] * mult2[1] + mult2[0] * mult1[1]
    multiplicacion = [a, b]
    return multiplicacion
def resta_complejos(res1, res2):
    """Función que retorna la resta de dos números complejos
    (list) -> (list)"""
    a = res1[0] - res2[0]
    b = res1[1] - res2[1]
    resta = [a, b]
    return resta
def division_complejos(div1, div2):
    """Función que retorna la division de dos números complejos
    (list) -> (list)"""
    denominador = div2[0]**2 + div2[1]**2
    numerador1 = (div1[0] * div2[0]) + (div1[1] * div2[1])
    numerador2 = div2[0]*div1[1] - div1[0]*div2[1]
    a = numerador1 / denominador
    b = numerador2 / denominador
    division = [a,b]
    return division
def modulo_complejo(complex):
    """Función que retorna el módulo de un número complejo
    (list) -> (list)"""
    num = complex[0]**2 + complex[1]**2
    modulo = math.sqrt(num)
    return modulo
def conjugado_complejo(complex):
    """Función que retorna el conjugado de un número complejo
    (list) -> (list)"""
    #(-1,0)
    a = complex[0]
    b = complex[1] * -1
    conjugado = [a, b]
    return conjugado
def polartocartesian(polar):
    """Función que retorna la conversión de polar a cartesiana de un número complejo.
    La fase se ingresa en grados y se realiza la conversión a radianes.
    (list) -> (list)"""
    fase = math.radians(float(polar[1]))
    a = polar[0]*math.cos(fase)
    b = polar[0]*math.sin(fase)
    cartesian = [a, b]
    return cartesian
def fase_complejos(polar):
    """Función que retorna la fase de un número complejo.
    (list) -> Float"""
    fase = math.atan(polar[1]/polar[0])
    return fase

