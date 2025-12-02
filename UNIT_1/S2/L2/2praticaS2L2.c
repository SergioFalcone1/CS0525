#include <stdio.h>
int main() {
    int numero1;
    int numero2;
    int media;
    printf("inserisci il primo numero: ");
    scanf("%d", &numero1);
    printf("inserisci il secondo numero: ");
    scanf("%d", &numero2);

    media = (numero1 + numero2) /2.0;
    printf("la media dei due numeri è:  %d", media);

    return 0;

}