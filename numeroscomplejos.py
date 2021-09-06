"""Librería Computación Cuántica: Números Complejos
Jaider Arley González Arias"""
import math
def suma_complejos(sum1, sum2):
    """Función que retorna la suma de dos números complejos
    (list) -> (list)"""
    a = sum1[0] + sum2[0]
    b = sum1[1] + sum2[1]
    suma = (a, b)
    return suma
def producto_complejos(mult1, mult2):
    """Función que retorna la multiplicación de dos números complejos
    (list) -> (list) """
    a = mult1[0] * mult2[0] - mult1[1] * mult2[1]
    b = mult1[0] * mult2[1] + mult2[0] * mult1[1]
    multiplicacion = (a, b)
    return multiplicacion
def resta_complejos(res1, res2):
    """Función que retorna la resta de dos números complejos
    (list) -> (list)"""
    a = res1[0] - res2[0]
    b = res1[1] - res2[1]
    resta = (a, b)
    return resta
def division_complejos(div1, div2):
    """Función que retorna la division de dos números complejos
    (list) -> (list)"""
    denominador = div2[0]**2 + div2[1]**2
    numerador1 = (div1[0] * div2[0]) + (div1[1] * div2[1])
    numerador2 = div2[0]*div1[1] - div1[0]*div2[1]
    a = numerador1 / denominador
    b = numerador2 / denominador
    division = (a,b)
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
    conjugado = (a, b)
    return conjugado
def polartocartesian(polar):
    """Función que retorna la conversión de polar a cartesiana de un número complejo.
    La fase se ingresa en grados y se realiza la conversión a radianes.
    (list) -> (list)"""
    fase = math.radians(float(polar[1]))
    a = polar[0]*math.cos(fase)
    b = polar[0]*math.sin(fase)
    cartesian = (a, b)
    return cartesian
def fase_complejos(polar):
    """Función que retorna la fase de un número complejo.
    (list) -> Float"""
    fase = math.atan(polar[1]/polar[0])
    return fase
def AdicionVectoresComplejos(v, w):
    r = [(0,0)]*len(v)
    for k in range(len(v)):
        r[k] = suma_complejos(v[k],w[k])
    return r
def SustracVectoresComplejos(v, w):
    r = [(0, 0)]*len(v)
    for k in range(len(v)):
        r[k] = resta_complejos(v[k], w[k])
    return r
def invvector(v):
    r = [(0, 0)] * len(v)
    for k in range(len(v)):
        r[k] = producto_complejos((-1,0),v[k])
    return r
def MultEscalarVector(c, v):
    r = [(0,0)] * len(v)
    for k in range(len(v)):
        r[k] = producto_complejos(c, v[k])
    return r
def AdicionMatriz(A,B):
    fila = [(0,0)] * len(A[0])
    r = [fila] * len(A)
    for j in range(len(A)):
        fila = [(0,0)] * len(A[0])
        r[j] = fila
        for k in range(len(A[0])):
            r[j][k] = suma_complejos(A[j][k],B[j][k])
    return r
def SustracMatriz(A, B):
    fila = [(0, 0)] * len(A[0])
    r = [fila] * len(A)
    for j in range(len(A)):
        fila = [(0, 0)] * len(A[0])
        r[j] = fila
        for k in range(len(A[0])):
            r[j][k] = resta_complejos(A[j][k], B[j][k])
    return r
def InversaAditivaMatriz(A):
    fila = [(0, 0)] * len(A[0])
    r = [fila] * len(A)
    for j in range(len(A)):
        fila = [(0, 0)] * len(A[0])
        r[j] = fila
        for k in range(len(A[0])):
            r[j][k] = producto_complejos((-1,0),A[j][k])
    return r
def MultEscalarMatriz(c, A):
    fila = [(0, 0)] * len(A[0])
    r = [fila] * len(A)
    for j in range(len(A)):
        fila = [(0, 0)] * len(A[0])
        r[j] = fila
        for k in range(len(A[0])):
            r[j][k] = producto_complejos(c, A[j][k])
    return r
def Transpuesta(A):
    t = []
    for k in range(len(A[0])):
        t.append([])
        for j in range(len(A)):
            t[k].append(A[j][k])
    return t
def ConjugadaMatVec(A):
    fila = [(0, 0)] * len(A[0])
    r = [fila] * len(A)
    for j in range(len(A)):
        fila = [(0, 0)] * len(A[0])
        r[j] = fila
        for k in range(len(A[0])):
            r[j][k] = conjugado_complejo(A[j][k])
    return r
def AdjuntaMatVec(A):
    return Transpuesta(ConjugadaMatVec(A))
def ProductMatrix(A,B):
    c = []
    for i in range(len(A)):
        c.append([])
        for j in range(len(B[0])):
            c[i].append((0,0))
            for k in range(len(A[0])):
                c[i][j] = suma_complejos(c[i][j],producto_complejos(A[i][k],B[k][j]))
    return c
def AccionMatVec(A,V):
    return ProductMatrix(A,V)
def ProductoInterno(V1,V2):
    return ProductMatrix(AdjuntaMatVec(V1),V2)[0][0]
def cartesiantopolar(a):
    p = math.sqrt((a[0]**2) + a[1]**2)
    tet = fase_complejos(a)
    return (p, tet)
def Norma(V):
    if ProductoInterno(V, V)[1] == 0:
        return math.sqrt(ProductoInterno(V, V)[0])
    else:
        a = cartesiantopolar(ProductoInterno(V, V))
        return (math.sqrt(a[0]), 0.5*a[1])
def DistanciaVec(v1,v2):
    if ProductoInterno(SustracMatriz(v1, v2), SustracMatriz(v1, v2))[1] == 0:
        return math.sqrt(ProductoInterno(SustracMatriz(v1,v2), SustracMatriz(v1,v2))[0])
    else:
        a = cartesiantopolar(ProductoInterno(
            SustracMatriz(v1,v2), SustracMatriz(v1,v2)))
        return (math.sqrt(a[0]), 0.5*a[1])
def Unitaria(A):
    m = ProductMatrix(AdjuntaMatVec(A), A)
    for i in range(len(m)):
        for j in range(len(m[0])):
            if i == j:
                if m[i][j] != (1,0):
                    return "No unitaria"
            else:
                if m[i][j] != (0,0):
                    return "No unitaria"
                else:
                    return "Unitaria"
def Hermitiana(A):
    Adjunta = AdjuntaMatVec(A)
    if Adjunta == A:
        return "Hermitiana"
    else:
        return "No es hermitiana"
def ProductTensor(A,B):
    columnas, filas = len(A)*len(B), len(A[0])*len(B[0])
    r, filas_usadas, columnas_usadas = [], 0, 0
    for i in range(filas):
        r.append([(0,0)]*columnas)
    for i in range(len(A)):
        matriz = MultEscalarMatriz(A[i], B)
        while filas_usadas != filas:
            while columnas_usadas < columnas:
                for l in range(len(B)):
                    for m in range(len(B[0])):
                        if filas_usadas == 0 and columnas_usadas == 0:
                            r[l][m] = matriz[l][m]
                        else:
                            r[l + filas_usadas][m + columnas_usadas] = matriz[l][m]
                columnas_usadas +=len(B)
            columnas_usadas = 0
            filas_usadas += len(B)
    return r
                            



