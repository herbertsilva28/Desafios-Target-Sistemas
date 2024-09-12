#include <stdio.h>

int main() {
    int INDICE = 13, SOMA = 0, K = 0;
    while (K < INDICE) {
        K = K + 1;
        SOMA = SOMA + K;
    }
    printf("%d\n", SOMA);
    return 0;
}

//Cálculo:

//K começa em 0.
//A cada iteração, K é incrementado por 1 e adicionado à SOMA.
//Isso continua enquanto K for menor que 13.
//Iterações:

//K = 1, SOMA = 1
//K = 2, SOMA = 3
//K = 3, SOMA = 6
//K = 4, SOMA = 10
//K = 5, SOMA = 15
//K = 6, SOMA = 21
//K = 7, SOMA = 28
//K = 8, SOMA = 36
//K = 9, SOMA = 45
//K = 10, SOMA = 55
//K = 11, SOMA = 66
//K = 12, SOMA = 78
//K = 13 (não entra no loop porque não é menor que 13)
//Portanto, SOMA = 78.