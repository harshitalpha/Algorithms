#include<stdio.h>
#include<conio.h>
#include<stdlib.h>
struct stackArray{
    char a[10];
    int top;
};

void push(struct stackArray * s, char ch)
{
    if((*s).top >= 10)
    {
        printf("Stack Over Flow");
        exit(0);
    }
    (*s).a[(*s).top] = ch;
    (*s).top ++ ;
    printf("Successfully added");
}

void printStack(struct stackArray s)
{
    while(1)
    {   s.top--;
        printf(" %c ->",s.a[s.top]);
        if(s.top <= 0 )
            break;
    }
}

int main()
{
    struct stackArray s;
    s.top = 0;
    push(&s,'A');
    push(&s,'B');
    push(&s,'c');
    printStack(s);
}
