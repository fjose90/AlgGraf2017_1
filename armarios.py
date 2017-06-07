from time import time
from math import sqrt


def armarios_n2(n):
    estados = [False] * (n+1)
    for crianca in range(1, n+1):
        for armario in range(1, n+1):
            if armario % crianca == 0:
                estados[armario] = not estados[armario]
    abertos = []
    for armario in range(1, n+1):
        if estados[armario]:
            abertos.append(armario)
    return abertos


def armarios_nlogn(n):
    estados = [False] * (n+1)
    for crianca in range(1, n+1):
        for armario in range(crianca, n+1, crianca):
            estados[armario] = not estados[armario]
    abertos = []
    for armario in range(1, n+1):
        if estados[armario]:
            abertos.append(armario)
    return abertos


def armarios_n(n):
    abertos = []
    for armario in range(1, n+1):
        raiz_quadrada = sqrt(armario)
        if raiz_quadrada == int(raiz_quadrada):
            abertos.append(armario)
    return abertos

def armarios_sqrtn(n):
    abertos = []
    i = 1
    armario = 1
    while armario <= n:
        abertos.append(armario)
        i += 1
        armario = i**2
    return abertos
    



N = int(input("Quantos armarios? "))

##inicio = time()
##print("\nquantidade de abertos = %d" % len(armarios_n2(N)))
##print("tempo (n2) = %.6f" % (time() - inicio))

inicio = time()
resultado = len(armarios_nlogn(N))
duracao = time() - inicio                
print("\nquantidade de abertos = %d" % resultado)
print("tempo (nlogn) = %.6f" % duracao)

inicio = time()
resultado = len(armarios_n(N))
duracao = time() - inicio                
print("\nquantidade de abertos = %d" % resultado)
print("tempo (n) = %.6f" % duracao)

inicio = time()
resultado = len(armarios_sqrtn(N))
duracao = time() - inicio                
print("\nquantidade de abertos = %d" % resultado)
print("tempo (sqrtn) = %.6f" % duracao)            

inicio = time()
resultado = int(sqrt(N))
duracao = time() - inicio                
print("\nquantidade de abertos = %d" % resultado)
print("tempo (1) = %.6f" % duracao)            
