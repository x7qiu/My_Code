#include <stdio.h>

struct Point{
    int x;
    int y;
};
typedef struct Point Point;

void PrintPoint(Point p){
    printf("%d\t%d\n", p.x, p.y);
}

// The only legal operations on a structure are:
// 1)copying it, 2)assigning to it, 3)taking its address(&), 4)acceessing its memeber

// As return value
Point MakePoint(int x, int y){
    Point temp;
    temp.x = x;
    temp.y = y;
    return temp;
}

int main(){
// Struct Initialization
// 1) directly
    Point x = {1, 2};

// 2) by field
    Point y = {.y = 2, .x = 1};

// 3) by copying
// using = is preferred over memcpy(q, p), altho still *shallow copy*
// compiler may opt to use memcpy 
    Point z = x;    
    PrintPoint(z);  // 1, 2

// Pointer to Struct
    Point* p = &x;
    p->x = 5;
    PrintPoint(x);  // 5,2

// Note:
// C does not allow recursive definition;
// So a sturct cannot contain itself, but could contain type of a pointer to itself


    return 0;
} 
