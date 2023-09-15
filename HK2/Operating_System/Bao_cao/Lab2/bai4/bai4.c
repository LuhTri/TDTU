#include <stdio.h>
#include <stdlib.h>

void main(int argc, char ** argv) {
    if (argc > 4) {
        printf("Qua nhieu doi so");
    }
    else {
        printf("Sum %d = %d", atoi(argv[1]), sum(atoi(argv[1])));
        printf("Fac %d! = %d", atoi(argv[2]), sum(atoi(argv[2])));
        div_n(atoi(argv[3]));
    }
    printf("\n");
}