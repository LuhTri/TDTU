#include <stdio.h>
#include <stdlib.h>

void bubbleSort(int arr[], int size) {
    int i, j, temp;

    for (i = 0; i < size - 1; i++) {
        for (j = 0; j < size - i - 1; j++) {
            if (arr[j] > arr[j + 1]) {
                //Swap arr[j] <=> arr[j - 1]
                temp = arr[j];
                arr[j] = arr[j + 1];
                arr[j + 1] = temp;
            }
        }
    }
}

void main(int argc, char ** argv) {
    //Loai bo cac doi so khong phai la so nguyen
    int n = argc - 1, index = 0;
    int arr[100];

    for (int i = 1; i < argc ; i++) {
        if (atoi(argv[i]) == 0) {
            n--;
        }
        else {
            arr[index] = atoi(argv[i]);
            index++;
        }
    }

    bubbleSort(arr, n);

    for (int i = 0; i < n; i++) {
        printf("%d\t", arr[i]);
    }

    printf("\n");
}