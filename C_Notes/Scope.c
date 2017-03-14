#include <stdio.h>
#include <string.h>

// The scope of a variable is the part of the program within which the name can be used. 
// There are 3 kind of variables, global, local, and formal parameters.

// Global variables: Defined outside of ALL functions. (C does not allow nested functions)
// Visible from the point where it's declared to the end of the file.

// Local variables: Defined inside a function or a block. Not visible outside.
// Takes precedence over global variable of the same name.

// Formal parameters: Defined in the function parameter. 
// Basically are just local variables.  
void fun1(){
    printf("g is NOT visible here.\n");
}
    
int g = 5;  

int main(){
    printf("g is visible here, its value is %d\n", g);

    int x = 10, y = 20;
    printf("x is %d here, y is %d.\n", x, y);   // x = 10, y = 20

    {
        int y = 40;
        x++;
        y++;
        printf("x is %d here, y is %d.\n", x, y);   // x = 11, y = 41
    }

        printf("x is %d here, y is %d.\n", x, y);   // x = 11, y = 20
    
    return 0;
}

int fun2(int h){
    printf("g is also visible here, %d\n", g);
    return g + h;
}


