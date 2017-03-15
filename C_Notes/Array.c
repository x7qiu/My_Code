#include <stdio.h>

int main(){
    int a[10] = {0,1,2,3,4,5,6,7,8,9};
    int* pa;

    pa = a;     // equivalent to pa = &a[0]
    int x = *pa;     // copy a[0] to x
    int y = *(++pa); // copy a[1] to y. Also notice ++pa evaluates to pa+1, whereas pa++ evaluates to pa
    printf("x is %d, y is %d.\n", x, y);

    int my_strlen(char* s);
    char b[] = "hello";
    x = my_strlen(b+2);         // length of "llo";
    printf("b+2 is %s\n", b+2); // llo
    printf("length of b+2 is %d\n", x); // 3

    void my_strcpy(char* s, char* t);
    char c[10];
    my_strcpy(c, b+2);
    puts(c);                    // llo
}
    

// One important difference between an array name and a pointer is that array name is not a variable.
// So pa = a and pa++ are legal, but a = pa and a++ are NOT.

// 1)
// When an array name is passed to a function, what is passed is the location of the initial element(a pointer).
// Within the called function, the argument is a local variable. 

// The private copy of s now points to end of string, but original variable still points to the beginning.
int my_strlen(char* s){
    int n;
    for (n=0; *s != '\0';s++)
        n++;
    return n;
}

// 2)
// As mentioned, since array name decays to a pointer when passed to a function, there are two implications.
// First, the length information is lost, since sizeof(arrayname) will only return size of a pointer.
// Second, you can modify indivisual element of the array, since you have access to the address.

// copy t to s;
void my_strcpy(char* s, char* t){
    while (*s++ = *t++)
        ;
}


