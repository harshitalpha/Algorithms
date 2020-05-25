#include"stack.c"

void stack_rev(ss * top,int x)
{
	if(isEmpty(*top))
		push(top,x);
	else
	{
		int a = pop(top);
		stack_rev(top,x);
		
		push(top,a);
	}
}

void reverse(ss * top)
{
	if(!isEmpty(*top))
	{
		int x = pop(top);
		reverse(top);
		
		stack_rev(top,x);
	}
}

void main()
{
	ss top = NULL;
	push(&top,3);
	push(&top,4);
	push(&top,6);
	push(&top,7);
	push(&top,1);
	push(&top,8);
	
	printStack(top);
	
	reverse(&top);
	printf("Hello");
	printStack(top);
}
