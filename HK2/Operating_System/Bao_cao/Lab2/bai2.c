#include <stdio.h>
#include <stdlib.h>

void main(int argc, char ** argv) {
	int n = atoi(argv[1]);
	
	if (n <= 0) {
		printf("Doi so khong phai la so nguyen duong\n");
	}
	else if (argc > 2) {
		printf("Co qua nhieu doi so\n");
	}
	else {
		//Tim uoc so cua doi so truyen vao
		int i;
		
		printf("Cac uoc so cua %d: ", n);
		for (i = 1; i <= n; i++) {
			if (n % i == 0) {
				printf("%d", i);
				if (i != n)
					printf(", ");
			}
		}

		//Phan tich doi so thanh thua so nguyen to
		int div = 2;
		printf("\n%d = ", n);
		while (n != 1) {
			if (n % div != 0) {
				div++;
			}
			else {
				n /= div;
				printf("%d", div);
				if (n != 1) 
					printf(" * ");
			}
		}
	}
	printf("\n");
}