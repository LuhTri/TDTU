#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <sys/time.h>
#include <sys/wait.h>
#include <sys/types.h>

struct timeval t_before, t_after, t_final;
int main(int argc, char ** argv) {
    gettimeofday(&t_before, NULL);

    int pid = fork();
    if (pid == 0) {
        system(argv[1]);
    }
    else if (pid > 0) {
        wait(NULL);
        gettimeofday(&t_after, NULL);
        timersub(&t_after, &t_before, &t_final);
        printf("Execution time: %ld.%.6ld\n", (long int)t_final.tv_sec, (long int)t_final.tv_usec);
    }

}