#include <stdio.h>

int main(){
    int a = 3;
    int b = 3;
    int b2 = a;
    // All 3 variables have different addresses; 
    // This is the "Classical model"". But in Python, "b2" and "a" would have the same address.
    printf("address of a is %p\n", (void*)&a);  //0x7fff53f7eb98
    printf("address of b is %p\n", (void*)&b);  //0x7fff53f7eb94
    printf("address of b2 is %p\n", (void*)&b2);//0x7fff53f7eb90

    struct Point{
        int x;
        int y;
    };
    struct Point pa = {3, 4};
    struct Point pb = pa;
    struct Point* pc = &pa;
    printf("address of pa is %p\n", (void*)&pa);    // address 1
    printf("address of pb is %p\n", (void*)&pb);    // address 2
    printf("value of pc is %p\n", (void*)pc);       // address 1
    printf("address of pc is %p\n", (void*)&pc);    // address 3
    
    int c[] = {1, 2, 3};
    int d[] = {1, 2, 3};
    int* e = c;
    printf("address of c is %p\n", (void*)c);   // address 1
    printf("address of d is %p\n", (void*)d);   // address 2
    printf("address of e is %p\n", (void*)e);   // address 1

    return 0;
}

// arrays created on stack can use sizeof(array)/sizeof(array[0])
// arrays created by malloc or passed as parameter can't do that, because sizeof(array) returns pointer size.
// In the latter case, has to pass an extra argument.
