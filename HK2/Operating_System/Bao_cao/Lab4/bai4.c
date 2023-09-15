#include <stdio.h>
#include <stdlib.h>
#include <pthread.h>
#include <unistd.h>

static long all_char;

typedef struct {
    char* source_file;
    char* target_file;
} file_t;

void* thr(void* ar) {
    file_t * ap = (file_t*)ar;
    FILE *f0, *f1;
    int count = 0;
    char c;

    f0 = fopen(ap->source_file, "r");
    f1 = fopen(ap->target_file, "w");

    while (c != EOF) {
        c = fgetc(f0);
        if (c != EOF) {
            fputc(c, f1);
        }
        count++;
    }

    all_char = count;
}

int main(int argc, char ** argv) {
    pthread_t tid;
    file_t f;

    f.source_file = argv[1];
    f.target_file = argv[2];

    pthread_create(&tid, NULL, thr, (void*)&f);
    pthread_join(tid, NULL);
    printf("Sao chep thanh cong %ld ki tu\n", all_char);
    
    printf("\n");
    return 0;
}