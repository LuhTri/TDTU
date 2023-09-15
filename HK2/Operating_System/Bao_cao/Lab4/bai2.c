#include <stdio.h>
#include <pthread.h>
#include <stdlib.h>
#include <sys/types.h>
#include <unistd.h>

int isPrimeNumber(int n) {
    int i;
    for (i = 2; i < n/2; i++) {
        if (n % i == 0)
            return 0;
    }

    return 1;
}

void* thr(void *ar) {
    int n = *((int *)ar);

    if (isPrimeNumber(n)) {
        printf("%d ", n);
    }
}

int main(int argc, char ** argv) {
    int n = atoi(argv[1]);
    int i = 2, num = 0;

    pthread_t tid[2];

    while (i < n) {
        num = i;
        pthread_create(&tid[0], NULL, thr, (void*)&num);
        pthread_join(tid[0], NULL);

        num = i + 1;
        pthread_create(&tid[1], NULL, thr, (void*)&num);
        pthread_join(tid[1], NULL);
        
        i += 2;
    }
    
    printf("\n");
    return 0;
}