#include<stdio.h>
#include<string.h>
#include<stdlib.h>

struct charstack
{
    char arr[100];
    int top;

};

void push(struct charstack *s , char ch)
{
    if(s->top >= 100)
    {
        printf("Stack Over Flow");
        exit(0);
    }
    s->arr[s->top] = ch;
    s->top ++;
}

char pop(struct charstack *s)
{
    if(s->top <= 0)
    {
        printf("Stack Under Flow");
        exit(0);
    }
    return s->arr[--(s->top)];

}


char * convert (char *infix)
{

}
