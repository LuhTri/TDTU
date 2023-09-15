#include <stdio.h>
#include <unistd.h>
#include <sys/wait.h>

int main(int argc, char ** argv) {
    pid_t pid_B = fork();

    //B
    if (pid_B == 0) {
        printf("\t- B[Pid:%d, PPid:%d]\n", getpid(), getppid());
        
        pid_t pid_D = fork();
        //D
        if (pid_D == 0) {
            printf("\t\t+ D[Pid:%d, PPid:%d]\n", getpid(), getppid());
        }
        //B
        else if (pid_D > 0) {
            pid_t pid_E = fork();

            //E
            if (pid_E == 0) {                
                printf("\t\t+ E[Pid:%d, PPid:%d]", getpid(), getppid());
            }
            //B
            else if (pid_B > 0) {
                return 0;
            }
        }
        
    }
    //A
    else if (pid_B > 0) {
        printf("> A[%d]\n", getpid());
        wait(NULL);

        
        pid_t pid_C = fork();
        //C
        if (pid_C == 0) {
            printf("\t- C[Pid:%d, PPid:%d]\n", getpid(), getppid());

            pid_t pid_H = fork();
            //H
            if (pid_H == 0) {
                printf("\t\t+ H[Pid:%d, PPid:%d]\n", getpid(), getppid());
            }
            //C
            else if (pid_H > 0) {
            }
        }
        //A
        else if (pid_C > 0) {
            printf("\n");
            return 0;
        }
    }   
}