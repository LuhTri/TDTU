#include <stdio.h>
#include <stdlib.h>
#include <unistd.h>
#include <string.h>

int main(int argc, char ** argv)
{
	int fp1[2], fp2[2], pid;
	
	if (pipe(fp1) == 0 && pipe(fp2) == 0) {
		pid = fork();
		if(pid == 0) {
			close(fp1[1]);
			int a, b;
			char temp[2];
			read(fp1[0], &a, sizeof(a));
			read(fp1[0], &b, sizeof(b));
			read(fp1[0], &temp, sizeof(temp));
			close(fp1[0]);
			
			int c = 0;
			if (strcmp(temp, "+") == 0) {
				c = a + b;
			} 
			else if (strcmp(temp, "-") == 0) {
				c = a - b;
			} 
			else if (strcmp(temp, "*") == 0) {
				c = a * b;
			} 
			else if (strcmp(temp, "/") == 0) {
				c = a / b;
			}
			close(fp2[0]);
			write(fp2[1], &c, sizeof(c));
			close(fp2[1]);
		}
		else {
			close(fp1[0]);
			int a = atoi(argv[1]);
			int b = atoi(argv[2]);
			write(fp1[1], &a, sizeof(a));
			write(fp1[1], &b, sizeof(b));
			write(fp1[1], argv[3], sizeof(argv[3]));
			close(fp1[1]);
			
			int n;
			close(fp2[1]);
			read(fp2[0], &n, sizeof(n));
			close(fp2[0]);
			printf("%d %s %d = %d\n", a, argv[3], b, n);
		}
	}
	return 0;
}