#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/wait.h>

int main(int argc, char ** argv) {
    pid_t pid = fork();

    int n = atoi(argv[1]);

    if (pid == 0) {
        printf("%d, ", n);
        while (n != 1) {
            if (n % 2 != 0) {
                n = 3*n + 1;
                printf("%d", n);
                if (n != 1) {
                    printf(", ");
                }
            }
            else {
                n /= 2;
                printf("%d", n);
                if (n != 1) {
                    printf(", ");
                }
            }
        }

        printf("\nTien trinh con ket thuc");

        return 0;
    }
    else if (pid > 0) {
        wait(NULL);

        return 0;
    }
}