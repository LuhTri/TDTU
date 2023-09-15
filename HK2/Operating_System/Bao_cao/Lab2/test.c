#include <stdio.h>
#include <stdlib.h>

void main(int argc, char ** argv) {
    int i, n = 10;
    
    printf("Divisor %d = ", n);
    for (i = 0; i <= n; i++) {
        // if (n % i == 0)
            printf("%d ", i);
    }
}