from time import time


memo_fib = None

def fatorial_nao_recursivo(n):
    resultado = 1
    for i in range(1, n+1):
        resultado *= i;
    return resultado

def fatorial_recursivo(n):
    if n <= 1:
        resultado = 1
    else:
        resultado = n * fatorial_recursivo(n-1)
    return resultado

def fib_nao_recursivo(n):
    a, b = 1, 1
    for _ in range(n-1):
        a, b = b, a+b
    return b

def fib_recursivo(n):
    if n <= 1:
        resultado = 1
    else:
        resultado = fib_recursivo(n-1) + fib_recursivo(n-2)
    return resultado

def fib_recursivo_com_memo(n):
    if memo_fib[n] is not None:
        return memo_fib[n]
    if n <= 1:
        resultado = 1
    else:
        resultado = fib_recursivo_com_memo(n-1) + \
                    fib_recursivo_com_memo(n-2)
    memo_fib[n] = resultado
    return resultado


'''
   Soma os dois parametros.
   Se um deles for None (indicando infinito), o resultado
   serah tambem None (infinito).
'''
def soma(x, y):
    if x is not None and y is not None:
        return x + y
    return None  

def floyd(matriz_adjacencias):
    n = len(matriz_adjacencias) - 1
    matriz = []
    for linha in range(n+1):
        matriz.append(matriz_adjacencias[linha][:])  # copia a linha

    for k in range(1, n+1):
        for i in range(1, n+1):
            for j in range(1, n+1):
                copia = False
                s = soma(matriz[i][k], matriz[k][j])
                if matriz[i][j] is None:
                    if s is not None:
                        copia = True
                else:
                    if s is not None and s < matriz[i][j]:
                        copia = True
                if copia:
                    matriz[i][j] = soma(matriz[i][k], matriz[k][j])

    return matriz

def minimo(x, y):
    if x is None:
        return y
    if y is None:
        return x
    return min(x, y)

def floyd_recursivo(M, i, j, k):
    if k==0:
        return M[i][j]
    if i==j:
        return 0
    custo_nao_usando_k = floyd_recursivo(M, i, j, k-1)
    custo_usando_k = soma(floyd_recursivo(M, i, k, k-1),
                          floyd_recursivo(M, k, j, k-1))
    return minimo(custo_nao_usando_k, custo_usando_k)

def floyd_top_down(matriz_adjacencias):
    n = len(matriz_adjacencias) - 1
    matriz = []
    for linha in range(n+1):
        matriz.append([None] * (n+1))  # copia a linha

    for i in range(1, n+1):
        for j in range(1, n+1):
            matriz[i][j] = floyd_recursivo(matriz_adjacencias, i, j, n) 
    return matriz




while True:
##    N = int(input("\nDigite um numero: "))
##    if N == 0:
##        break

##    inicio = time()
##    fib = fib_nao_recursivo(N)
##    fim = time()
##    print("fibonacci(%d) = %d" % (N, fib))
##    print("tempo (nao-recursivo) = %.6f" % (fim - inicio))

##    inicio = time()
##    fat = fib_recursivo(N)
##    fim = time()
##    print("fibonacci(%d) = %d" % (N, fib))
##    print("tempo (recursivo) = %.6f" % (fim - inicio))

##    inicio = time()
##    memo_fib = [None] * (N+1)  # cria o memo para subproblemas
##    fat = fib_recursivo_com_memo(N)
##    fim = time()
##    print("fibonacci(%d) = %d" % (N, fib))
##    print("tempo (recursivo com memo) = %.6f" % (fim - inicio))
    
    grafo = [[], \
             [None, 0, 5, 9, None], \
             [None, None, 0, 2, None], \
             [None, 4, 1, 0, None], \
             [None, 1, None, None, 0]]

    inicio = time()
    resultado_floyd = floyd(grafo)
    fim = time()
    for linha in range(1, len(grafo)):
        for coluna in range(1, len(grafo)):
            print(resultado_floyd[linha][coluna], end=" ")
        print()
    print("tempo (PD bottom up) = %.6f" % (fim - inicio))

    inicio = time()
    resultado_floyd = floyd_top_down(grafo)
    fim = time()
    for linha in range(1, len(grafo)):
        for coluna in range(1, len(grafo)):
            print(resultado_floyd[linha][coluna], end=" ")
        print()
    print("tempo (recursivo) = %.6f" % (fim - inicio))

    break

    

