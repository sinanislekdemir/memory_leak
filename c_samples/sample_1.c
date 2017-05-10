#include <stdio.h>
#include <stdlib.h>

#define SIZE 1024*1024


int main()
{
    char * data = malloc(SIZE);
    char * other_data = malloc(SIZE);
    data = other_data;
}
