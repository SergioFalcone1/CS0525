#include <stdio.h>

int main() {   
    int numero1;
    int numero2;
    int prodotto;

    printf("inserisci il primo numero: ");
    scanf("%d", &numero1);

    printf("inserisci il secondo numero: ");
    scanf("%d", &numero2);

    prodotto = numero1 * numero2;

    printf("il risultato è: %d\n", prodotto);

    return 0;
}