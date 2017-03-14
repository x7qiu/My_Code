#include <stdio.h>
#include <stdlib.h>

/*
1. A static variable inside a function keeps its value between invocations.
2. A static global variables or a function is “seen” only in the translation unit it’s declared in.(encapsulation)
*/

void foo(){
    int a = 10;
    static int sa = 10;
    
    a += 5;
    sa += 5;
    printf("a = %d, sa = %d\n", a, sa);
}

char* bar(){
    static char text2[10] = "qiuxie";
    return (text2);             // Not recommended, but safe. Not thread-safe. 
}

int  main(){
    int i;
    for (i=0; i<10; i++){
        foo();
        // a = 15, sa = 15
        // a = 15, sa = 20
        // a = 15, sa = 25
        // ......
    }
    // but sa is not visible here, outside of the function
    
    char* text1;
    text1 = bar();          
    puts(text1);
    return 0;

}
