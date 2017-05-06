#include <stdlib.h>
#include <stdio.h>
#include <math.h>
#include <time.h>
#include <sys/timeb.h>

typedef struct {
    int n_elementos;
    int peso_total;
    int valor_total;
    int *elementos;
} MOCHILA;

void inicializar_mochila(MOCHILA *mochila, int n_items) {
    mochila->n_elementos = 0;
    mochila->peso_total = 0;
    mochila->valor_total = 0;
    mochila->elementos = (int*) malloc(n_items * sizeof(int));
}

void mochila_enumeracao_total(int n_items,
                              int *pesos, int *valores, int peso_limite) {
    int max_valor = 0;
    int melhor_subconjunto = 0;
    long long int n_subconjuntos = pow(2, n_items);

    for (long long int subconjunto = 0; subconjunto < n_subconjuntos; subconjunto++) {
        int peso_subconjunto = 0;
        int valor_subconjunto = 0;
        for (int item = 0; item < n_items; item++) {
            if (subconjunto & (1<<item)) {
                peso_subconjunto += pesos[item];
                if (peso_subconjunto > peso_limite) {
                    valor_subconjunto = 0;
                    break;
                }
                valor_subconjunto += valores[item];
            }
        }
        if (valor_subconjunto > max_valor) {
            max_valor = valor_subconjunto;
            melhor_subconjunto = subconjunto;
        }
    }

    printf("\nValor otimo: %d", max_valor);
    printf("\n\nElementos:");
    for (int item = 0; item < n_items; item++) {
        if (melhor_subconjunto & (1<<item)) {
            printf("\n%d(valor: %d, peso: %d)", item, valores[item], pesos[item]);
        }
    }
}

void copiar_mochila(MOCHILA *mochila_origem, MOCHILA *mochila_destino) {
    mochila_destino->n_elementos = mochila_origem->n_elementos;
    mochila_destino->peso_total = mochila_origem->peso_total;
    mochila_destino->valor_total = mochila_origem->valor_total;
    for (int i = 0; i < mochila_origem->n_elementos; i++) {
        mochila_destino->elementos[i] = mochila_origem->elementos[i];
    }
}

void backtrack(int n_items, int *pesos, int *valores, int peso_limite,
               MOCHILA *estado_corrente, MOCHILA *melhor_mochila) {
    // testa se eh a melhor mochila que voce ja viu
    if (estado_corrente->valor_total > melhor_mochila->valor_total) {
        copiar_mochila(estado_corrente, melhor_mochila);
    }

    int proximo_candidato = 0;
    int tamanho = estado_corrente->n_elementos;
    if (estado_corrente->n_elementos > 0) {
        proximo_candidato = estado_corrente->elementos[tamanho-1] + 1;
    }
    for (int item = proximo_candidato; item < n_items; item++) {
        if (estado_corrente->peso_total + pesos[item] > peso_limite) {
            continue;
        }
        // acrescenta o novo item (SUJOU)
        estado_corrente->n_elementos++;
        estado_corrente->peso_total += pesos[item];
        estado_corrente->valor_total += valores[item];
        estado_corrente->elementos[tamanho] = item;

        backtrack(n_items, pesos, valores, peso_limite,
                  estado_corrente, melhor_mochila);

        // remove o item que tinha sido acrescentado (LIMPOU)
        estado_corrente->n_elementos--;
        estado_corrente->peso_total -= pesos[item];
        estado_corrente->valor_total -= valores[item];
    }
}

void mochila_backtracking(int n_items,
                          int *pesos, int *valores, int peso_limite) {
    MOCHILA estado_corrente, melhor_mochila;
    inicializar_mochila(&estado_corrente, n_items);
    inicializar_mochila(&melhor_mochila, n_items);
    backtrack(n_items, pesos, valores, peso_limite,
              &estado_corrente, &melhor_mochila);

    printf("\nValor otimo: %d", melhor_mochila.valor_total);
    printf("\n\nElementos:");
    for (int i = 0; i < melhor_mochila.n_elementos; i++) {
        int item = melhor_mochila.elementos[i];
        printf("\n%d(valor: %d, peso: %d)", item, valores[item], pesos[item]);
    }
}

int sorteie(int a, int b) {
    return rand() % (b-a+1) + a;
}

int main() {
    srand(time(NULL));
    struct timeb inicio, fim;

    int n = 30;
    int capacidade_mochila = 100;
    int *pesos = (int*) malloc(n * sizeof(int));
    int *valores = (int*) malloc(n * sizeof(int));
    for (int i = 0; i < n; i++) {
        pesos[i] = sorteie(1, 4);
        valores[i] = sorteie(1, 1000);
    }

    ftime(&inicio);
    mochila_enumeracao_total(n, pesos, valores, capacidade_mochila);
    ftime(&fim);
    printf("\n\nTempo (por enumeracao): %d milissegundos",
           (int) 1000.0 * (fim.time - inicio.time) + fim.millitm - inicio.millitm);
    printf("\n\n");

    ftime(&inicio);
    mochila_backtracking(n, pesos, valores, capacidade_mochila);
    ftime(&fim);
    printf("\n\nTempo (por backtracking): %d milissegundos",
           (int) 1000.0 * (fim.time - inicio.time) + fim.millitm - inicio.millitm);
    printf("\n\n");
}
