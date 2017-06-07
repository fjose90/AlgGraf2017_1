from time import time


memo = {}

def cont_seq_enumeracao(n):
    contador = 0
    maior_seq = 2**n - 1
    for numero_seq in range(maior_seq + 1):
        seq = bin(numero_seq)[2:]
        seq_ok = True
        for indice in range(len(seq) - 1):
            if seq[indice] == seq[indice + 1] == '1':
                seq_ok = False
                break
        if seq_ok:
            contador += 1
    return contador

def cont_seq_backtracking(n):

    def busca_prof(n, seq_corrente, cont_ptr):
        if len(seq_corrente) == n:
            cont_ptr[0] += 1  # incrementa o contador
            return
        for proximo_bit in [0,1]:
            if proximo_bit == 0 or \
               len(seq_corrente) == 0 or \
               seq_corrente[-1] == 0:
                # cria o novo estado
                seq_corrente.append(proximo_bit)
                # chama recursivamente
                busca_prof(n, seq_corrente, cont_ptr)
                # volta ao estado original
                del(seq_corrente[-1])
        
    contador = [0]
    busca_prof(n, [], contador)
    return contador[0]
    
def cont_seq_recursivo(n):
    if n == 0:
        return 1
    if n == 1:
        return 2
    return cont_seq_recursivo(n-1) + \
           cont_seq_recursivo(n-2)

def cont_seq_PD_topdown(n):
    resultado_memo = memo.get(n)
    if resultado_memo is not None:
        return resultado_memo
    
    if n == 0:
        resultado = 1
    elif n == 1:
        resultado = 2
    else:
        resultado = cont_seq_PD_topdown(n-1) + \
                    cont_seq_PD_topdown(n-2)

    memo[n] = resultado
    return resultado

def cont_seq_PD(n):
    respostas = [None] * (n+1)
    respostas[0] = 1
    respostas[1] = 2
    for x in range(2, n+1):
        respostas[x] = (respostas[x-1] + respostas[x-2]) % 1000
    return respostas[n]


n = int(input("\nDigite n: "))

##inicio = time()
##resultado = cont_seq_enumeracao(n)
##duracao = time() - inicio
##print("Resultado = %d" % resultado)
##print("Tempo (enumeracao) = %.6f" % duracao)

##inicio = time()
##resultado = cont_seq_backtracking(n)
##duracao = time() - inicio
##print("Resultado = %d" % resultado)
##print("Tempo (backtracking) = %.6f" % duracao)

##inicio = time()
##resultado = cont_seq_recursivo(n)
##duracao = time() - inicio
##print("Resultado = %d" % resultado)
##print("Tempo (recursivo) = %.6f" % duracao)

##inicio = time()
##resultado = cont_seq_PD_topdown(n)
##duracao = time() - inicio
##print("Resultado = %d" % resultado)
##print("Tempo (PD topdown) = %.6f" % duracao)

inicio = time()
resultado = cont_seq_PD(n)
duracao = time() - inicio
print("Resultado = %d" % resultado)
print("Tempo (PD bottomup) = %.6f" % duracao)
        
        
        
    


            
