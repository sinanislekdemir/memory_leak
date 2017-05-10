#include <stdio.h>
#include <stdlib.h>

void func ()
{
    char * data = malloc(10000);
}
 
int main ( )
{
    for(int i = 0; i < 10000; i++)
        func();
}
