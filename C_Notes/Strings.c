#include <stdio.h>
#include <stdlib.h>
#include <string.h>


int  main(){
// Several ways to "produce" a string

    // 1)
    char* str1 = "haha1";
    printf("str1 is %s, with value str1 %p, with address &str1 %p\n", str1, (void*)str1, &str1);

    str1 = "haha2";
    printf("str1 is %s, with value str1 %p, with address &str1 %p\n", str1, (void*)str1, &str1);
    // st1 is pointer to some string literal.
    // Different str1, same &str1.
/*
The syntax char* str1 = "haha1" points a char pointer str1 to a read-only string literal.
Making changes such as str[0] = 'H' is illegal.

With str1 = "haha2", str is pointing to another read-only string literal.
So str1 now have a different value equaling the address of the new string literal, but the address of str1, aka. &str1, remains unchanged.
*/
    
    // 2)
    char str2[] = "xixi1";
    str2[0] = 'X';
    printf("str2 is %s, with value str2 %p, with address &str2 %p\n", str2, (void*)str2, &str2);

    strcpy(str2, "xixi2");
    printf("str2 is %s, with value str2 %p, with address &str2 %p\n", str2, (void*)str2, &str2);
    //Results in same str2 in %p and same &str2.
/*
The syntax char str2[] = "xixi1" INITIALIZE a char array, equiavlent to char str2[] = {'x', 'i', 'x', 'i', 0}. 
Making changes to such a char array is legal. 
However, once the char array is initialized, it cannot be reassigned by simply using "=". 
This is because string is NOT a primitive type in C, and array doesn't support assignment, so that char array assignment with "=" is not supported. 
Instead, a library function such as strcpy, strncpy, or memcpy should be used. 
Modifying a char array does not change the value of str2, which is the memory address of the first char in the array.
*/
    // 3)
    char* str3 = malloc(sizeof(char)* 10);
    strcpy(str3, "hehe");
    str3[0] = 'G';
    printf("str3 is %s, with value str3 %p, with address &str3 %p\n", str3, (void*)str3, &str3);

    strcpy(str3, "GeGe");
    printf("str3 is %s, with value str3 %p, with address &str3 %p\n", str3, (void*)str3, &str3);
    
    free(str3);
    return 0;
    //Results in same str3 and &str3

}

//More Comments:
/*
A string literal can be used in two slightly different ways:
1. As the initializer for an array of char. It specifies the initial values of the characters in that array.
2. Anywhere else, it turns into an unnamed, static array of characters, and this unnamed array may be stored in read-only memory, and which therefore cannot necessarily be modified. 
In an expression context, the array is converted at one to a pointer. So char* p = "string literal" initilizes p to point to the unnamed array's first element.

Just to illustrate again:
char message[] = "hello";       // message is a char array
char* pmessage = "hello";        // pmessage is a pointer
*/

