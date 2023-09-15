#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

int main(int argc, char ** argv) {
    pid_t pid_B, pid_C;

    pid_B = fork();

    //B
    if (pid_B == 0) {}
    //A
    else if (pid_B > 0) {
        pid_C = fork();

        //C
        if (pid_C == 0) {}
        //A
        else if (pid_C > 0) {}
    }



}