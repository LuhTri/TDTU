#include <stdio.h>
#include <unistd.h>
#include <string.h>
#include <stdlib.h>
#include <sys/wait.h>

int main(int argc, char **argv)
{
    int fp1[2], fp2[2];
    int pid, buffer, i;

    if (argc < 2)
    {
        printf("Thieu doi so");
        return -1;
    }

    if (pipe(fp1) == 0 && pipe(fp2) == 0)
    {
        pid = fork();

        if (pid < 0)
        {
            printf("Fork faild\n");
            return -1;
        }
        else if (pid == 0)
        {
            close(fp1[1]);
            close(fp2[0]);
            for (i = 1; i <= argc; i++)
            {
                read(fp1[0], &buffer, sizeof(buffer));
                printf("Read from parents: %d\n", buffer);
                int t = 1;
                write(fp2[1], &t, sizeof(t));
            }
            close(fp1[0]);
            close(fp2[1]);
        }
        else
        {
            close(fp1[0]);
            close(fp2[1]);
            printf("Data send from parents: %s\n", argv[1]);

            for (i = 1; i <= argc; i++)
            {
                // int len = strlen(argv[i]);
                int temp = atoi(argv[i]);
                write(fp1[1], &temp, sizeof(temp));
                printf("Da viet\n");
                int t;
                read(fp2[0], &t, sizeof(t));
            }
            close(fp1[1]);
            close(fp2[0]);
        }
    }
    else
    {
        printf("Pipe failed\n");
        return -2;
    }
}
