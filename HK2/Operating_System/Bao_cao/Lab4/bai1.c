#include <stdio.h>
#include <pthread.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

struct arr {
    int n;
    int a[10];
};

void* thr1(void* ar) {
    int count, sum = 0;
    struct arr *ap = (struct arr*) ar;

    for (count = 0; count < ap->n; count++)
        sum += ap->a[count];

    float tbc = (float)sum/ap->n;
    printf("TrungBinhCong: %4.3f\n", tbc);
}

void* thr2(void* ar) {
    struct arr *ap = (struct arr*)ar;
    int count, min = ap->a[0];

    for (count = 1; count < ap->n; count++) {
        if (min > ap->a[count])
            min = ap->a[count];
    }

    printf("Min: %d\n", min);
}

void* thr3(void* ar) {
    struct arr *ap = (struct arr*)ar;
    int count, max = ap->a[0];

    for (count = 1; count < ap->n; count++) {
        if (max < ap->a[count])
            max = ap ->a[count];
    }

    printf("Max: %d\n", max);
}

int main(int argc, char * argv[]) {
    struct arr ar;
    ar.n = argc - 1;
    int i;

    for (i = 1; i < argc; i++) {
        ar.a[i - 1] = atoi(argv[i]);
    }

    pthread_t tid[3];
    pthread_create(&tid[0], NULL, thr1, (void*)&ar);
    sleep(2);
    pthread_create(&tid[1], NULL, thr2, (void*)&ar);
    sleep(2);
    pthread_create(&tid[2], NULL, thr3, (void*)&ar);
    sleep(2);

    return 0;
}