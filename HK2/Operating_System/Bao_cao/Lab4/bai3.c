#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <sys/time.h>

typedef struct {
    char* source_file1;
    char* source_file2;
    char* result_file;
} file_t;

void* thr(void* ar) {
    file_t *ap = (file_t*)ar;
    FILE *f1, *f2, *result;
    int row, column, i, j;

    f1 = fopen(ap->source_file1, "r");
    f2 = fopen(ap->source_file2, "r");
    result = fopen(ap->result_file, "w");

    fscanf(f1, "%d\n", &row);
    fscanf(f1, "%d\n", &column);
    fscanf(f2, "%d\n", &row);
    fscanf(f2, "%d\n", &column);

    int A[row][column], B[row][column], C[row][column];
    for (i = 0; i < row; i++) {
        for (j = 0; j < column; j++) {
            fscanf(f1, "%d", &A[i][j]);
            fscanf(f2, "%d", &B[i][j]);
            C[i][j] = A[i][j] + B[i][j];
        }
        fscanf(f1, "\n");
    }

    for (i = 0; i < row; i++) {
        for (j = 0; j < column; j++) {
            fprintf(result, "%d ", C[i][j]);
        }
        fprintf(result, "\n");
    }
}

int main(int argc, char  *argv[]) {
    file_t f;
    struct timeval tv;
    time_t curtime;
    char buffer[30];

    gettimeofday(&tv, NULL);
    curtime = tv.tv_sec;
    strftime(buffer, 30, "%m-%d-%Y %T.", localtime(&curtime));
    printf("%s and %ld\n", buffer, tv.tv_usec);

    f.source_file1 = argv[1];
    f.source_file2 = argv[2];
    f.result_file = argv[3];

    pthread_t tid;
    pthread_create(&tid, NULL, thr, (void*)&f);
    pthread_join(tid, NULL);

    return 0;
}
