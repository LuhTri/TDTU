#include <stdio.h>
#include <unistd.h>
#include <stdlib.h>
#include <sys/wait.h>

int main(int argc, char ** argv) {
    pid_t pid;
    pid = fork();

    int n = atoi(argv[1]);

    if (pid == 0) {
        int S1 = 0, i;

        for (i = 1; i <= n; i++) {
            if (n % i == 0)
                S1 += i;
        }

        printf("Tong cac uoc so cua %d: %d\n", n, S1);

        return 0;
    }
    else if (pid > 0) {
        int S2 = 0, i;

        for (i = 0; i <= n; i++) {
            S2 += i;
        }

        wait(NULL);
        printf("Tong cac so tu 1 den %d: %d", n, S2);

        return 0;
    }
}