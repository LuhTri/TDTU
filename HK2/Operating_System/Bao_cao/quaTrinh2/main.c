#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/ipc.h>
#include <sys/msg.h>
#include <semaphore.h>

#define SEED 200	   // sinh so ngau nhien
#define UPPER_LIM 1000 // so ngau nhien lon nhat
#define LOWER_LIM 1	   // so ngau nhien nho nhat

// khai bao ham
int generate_random_number(unsigned int lower_limit, unsigned int upper_limit);
// khai bao cau truc de luu tru du lieu

struct data
{
	long mesg_type;
	int n;				  // so phan tu cua mang
	int a[UPPER_LIM];	  // cac phan tu  cua mang
} array1, array2, array3; // cac bien struct su dung trong bai

// Tao thread de khoi tao cac phan tu cua mang
void *init_data(void *array) {
	int *a = (int*)array;

	int i;
	for (i = 0; i < array1.n; i++) {
		a[i] = generate_random_number(LOWER_LIM, UPPER_LIM);
	}

	return NULL;
}

// Ham noi mang sau khi chay thread
void merge_data(struct data array1, struct data array2, void *array3)
{
	struct data *ap = (struct data *)array3;
	ap->n = array1.n + array2.n;
	int i;
	for (i = 0; i < array1.n; i++)
		ap->a[i] = array1.a[i];
	for (i = 0; i < array2.n; i++)
	{
		int temp = array1.n + i;
		ap->a[temp] = array2.a[i];
	}
}

// Ham luu du lieu vao file
void Save_file(struct data array) {
	FILE *fp = fopen("init_data", "w");

	if (fp == NULL) {
		printf("Cannot open file\n");
		return;
	}

	printf("Ket qua: ");
	int i;
	for (i = 0; i < array.n; i++) {
		fprintf(fp, "%d\n", array.a[i]);
		printf("%d\n", array.a[i]);
	}
	fclose(fp);
	printf("\n");
}

struct message {
	long msg_type;
	struct data array;
 } message;

int main(int argc, char *argv[])
{
	// Truyen doi so n la so phan tu cua mang.
	array1.n = atoi(argv[1]) / 2;
	array2.n = atoi(argv[1]) - array1.n;

	// Tao ra 2 thread voi so phan tu truyen vao nhu tren, khoi tao phan tu cua mang
	pthread_t tid1, tid2;
	pthread_create(&tid1, NULL, init_data, array1.a);
	pthread_create(&tid2, NULL, init_data, array2.a);

	pthread_join(tid1, NULL);
	pthread_join(tid2, NULL);


	// Sau khi khoi tao se noi 2 chuoi cua 2 thread vao 1 chuoi chung va save file
	merge_data(array1, array2, (void *)&array3);
	Save_file(array3);

	// Hay tao ra message queue gui ket qua cua array3 o tren sang chuong trinh solve.c
	key_t key;
	int msgid;

	key = ftok("msg", 1);
	msgid - msgget(key, IPC_CREAT | 0666);
	message.msg_type = 1;
	message.array = array3;
	msgsnd(msgid, &message, 1024, 0); 

	return 0;
}

// ham sinh so ngau nhien
int generate_random_number(unsigned int lower_limit, unsigned int upper_limit)
{
	return (rand() % (lower_limit + (upper_limit - lower_limit)));
}
