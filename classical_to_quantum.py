import math

def suma(a,b):
    return (a[0]+b[0],a[1]+b[1])


def multiplicacion(a,b):
    return (a[0]*b[0]-a[1]*b[1],a[0]*b[1]+a[1]*b[0])


def modulo(c):
    result = math.sqrt(c[0]**2 + c[1]**2)
    return result


def matrizxmatriz(matriz1: list, matriz2: list):
    filas = len(matriz1)
    columnas = len(matriz2[0])
    res = [[(0, 0) for i in range(columnas)] for j in range(filas)]
    for i in range(0, filas):
        for j in range(0, columnas):
            temp = (0, 0)
            for k in range(0, len(matriz2)):
                temp = suma(temp, multiplicacion(matriz1[i][k], matriz2[k][j]))
            res[i][j] = temp
    return res


def transponer(a: list):
    result = list()
    for i in range(len(a[0])):
        result.append([])
        for j in range(len(a)):
            result[i].append("None")

    for i in range(len(a)):
        for j in range(len(a[i])):
            result[j][i] = a[i][j]
    return result


def t_clics(a, t):
    res = [[a[j][i] for i in range(len(a[0]))] for j in range(len(a))]
    for i in range(t-1):
        res = matrizxmatriz(res, a)
    return res


def click(matriz: list, vector: list):
    ans = [[0 for i in range(len(vector[0]))] for j in range(len(matriz))]
    for i in range(len(matriz)):
        for j in range(len(vector[0])):
            for k in range(len(matriz[0])):
                ans[i][j] = ans[i][j] + (matriz[i][k] * vector[k][j])

    return ans


def problem_canicas(matriz: list, vector: list, clicks: int):
    for i in range(len(matriz)):
        for j in range(len(matriz[0])):
            if matriz[j][i]:
                matriz[j][i] = 1
            else:
                matriz[j][i] = 0
    for i in range(clicks):
        vector = click(matriz, vector)

    return vector


def rendijas_reales(matriz: list, vector: list, clicks: int):
    for i in range(clicks):
        vector = click(matriz, vector)

    return vector


def vector_final_real(num_rendijas):
    vectori = [[(0, 0)] for i in range(2+3*num_rendijas)]
    vectori[0][0] = (1, 0)
    return transponer(matrizxmatriz(t_clics(multiples_rendijas_real(num_rendijas), 2), vectori))


def multiples_rendijas_real(r):
    n = 2+3*r
    matriz = [[(0, 0) for i in range(n)] for j in range(n)]
    for i in range(1, r+1):
        matriz[i][0] = (1/r, 0)
    temp = r+1
    for j in range(1, int(r+1)):
        matriz[temp][j] = (1/3, 0)
        matriz[temp+1][j] = (1/3, 0)
        matriz[temp+2][j] = (1/3, 0)
        temp += 2
    for i in range(r+1, n):
        matriz[i][i] = (1, 0)

    return matriz


def multiples_rendijas_imaginario(r):
    n = 2+3*r
    matriz = [[(0, 0) for i in range(n)] for j in range(n)]
    for j in range(1, r+1):
        matriz[j][0] = (1/(2**0.5), 0)
    temp = r+1
    for j in range(1, r+1):
        matriz[temp][j] = (-1/(6**0.5), 1/(6**0.5))
        matriz[temp+1][j] = (-1/(6**0.5), -1/(6**0.5))
        matriz[temp+2][j] = (1/(6**0.5), -1/(6**0.5))
        temp += 2
    for i in range(r+1, n):
        matriz[i][i] = (1, 0)

    return matriz


def vector_final_imaginario(num_rendijas):
    vectori = [[(0, 0)] for i in range(2+3*num_rendijas)]
    vectori[0][0] = (1, 0)
    return transponer(matrizxmatriz(t_clics(multiples_rendijas_imaginario(num_rendijas), 2), vectori))