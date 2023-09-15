#include <pthread.h>
#include <stdio.h>
#include <stdlib.h>
#include <sys/ipc.h>
#include <sys/msg.h>
#include <semaphore.h>
#include <math.h>

#define UPPER_LIM 1000 // so ngau nhien lon nhat
int isPrime(int n);	   // ham kiem tra so nguyen to
int isSquare(int n);   // ham kiem tra so chinh phuong

// khai bao cau truc de luu tru du lieu
struct data
{
	long mesg_type;
	int n;			  // so phan tu cua mang
	int a[UPPER_LIM]; // cac phan tu  cua mang
} array;

sem_t mutex1, mutex2;
// pthread_mutex_t mutex;
// thread de kiem tra phan tu nao la nguyen to
void *prime(void *array)
{
	struct data *ap = (struct data*) array;

	int i;
	for (i = 0; i < ap->n; i++) {
		if (isPrime(ap->a[i])) {
			sem_wait(&mutex1);
			printf("Thread prime saw %d is prime\n", ap->a[i]);
			sem_post(&mutex2);
		}
	}
}
// thread de kiem tra phan tu nao so chinh phuong
void *square(void *array)
{
	struct data *ap = (struct data*) array;

	int i;
	for (i = 0; i < ap->n; i++) {
		if (isSquare(ap->a[i])) {
			sem_wait(&mutex2);
			printf("Thread prime saw %d is square\n", ap->a[i]);
			sem_post(&mutex1);
		}
	}
}

struct message {
	long msg_type;
	struct data array;
} message;

int main()
{
	// Hay viet message queue de nhan gia tri array tu main gui qua
	key_t key;
	int msgid;

	key = ftok("msg", 1);
	msgid - msgget(key, IPC_CREAT | 0666);
	msgrcv(msgid, &message, 1024, 1, 0);

	// Thuc hien goi 2 thread thuc thi nhu da khai bao
	pthread_t tid1, tid2;
	pthread_create(&tid1, NULL, prime, &message.array);
	pthread_create(&tid2, NULL, prime, &message.array);

	msgctl(msgid, IPC_RMID, NULL);

	return 0;
}

// Ham kiem tra so nguyen to
int isPrime(int n)
{
	if (n < 2)
		return 0;

	int square = (int)sqrt(n);
	int i;

	for (i = 2; i <= square; i++)
		if (n % i == 0)
			return 0;
	return 1;
}

// Ham kiem tra so chinh phuong
int isSquare(int n)
{
	int sqr = sqrt(n);
	if (sqr * sqr == n)
		return 1;
	else
		return 0;
}
