#include <stdlib.h>
#include <stdio.h>

typedef struct{
    int* array;
    int size;
    int used;
} Array;

void initArray(Array* nums, size_t initialSize){
    nums->array = malloc(initialSize* sizeof(int));
    nums->size = initialSize;
    nums->used = 0;
}

void insertArray(Array* nums, int element){
    if (nums->used == nums->size){
        nums->size *= 2;
        nums->array = realloc(nums->array, nums->size * sizeof(int));
    }

    (nums->array)[nums->used] = element;
    (nums->used) ++;

}

int popArray(Array* nums){
    if (nums->used < (nums->size)/3){
        nums->size /= 2;
        nums->array = realloc(nums->array, nums->size * sizeof(int));
    }

    int val = (nums->array)[nums->used];
    (nums->used)--;

    return val;
}

void copyArray(Array* nums, int* source, int len){
    void freeArray(Array* nums);
    freeArray(nums);

    nums->array = malloc(len * sizeof(int));
    nums->size = len;
    nums->used = len;

    int i;
    for (i=0; i<len; i++){
        (nums->array)[i] = source[i];
    }
}
    
void freeArray(Array* nums){
    free(nums->array);
    nums->size = 0;
    nums->used = 0;
}

void printArray(Array* nums, int len){
    int i;
    for (i=0; i<len; i++){
        printf("%d", (nums->array)[i]);
    }
    printf("\n");    
}

int main(){
    int* nums = {0,1,2,3};

    Array a;
    initArray(&a, 5);

    int i;
    for (i=0; i<5; i++){
        insertArray(&a, i);
    }
    insertArray(&a,5);
    insertArray(&a,6);
    popArray(&a);
    printArray(&a,a.used);
    

    freeArray(&a);

    return 0;
}
    
