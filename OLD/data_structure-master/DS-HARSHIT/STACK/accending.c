#include"stack.c"

void main()
{
	ss top = NULL;
	
	char ans = 'y';
	int x;
	int n = 0;
	while(ans == 'y' || ans == 'Y')
	{
		printf("Enter The Number To push in Stack :- ");
		scanf("%d",&x);
		push(&top,x);
		n++;
		printf("Do Yoy Want To Enter More Elemens :- ");
		scanf(" %c",&ans);
	}
	printStack(top);
	
	ss top2 = NULL;
	
	while(!isEmpty(top))
	{
		x = pop(&top);
		if(isEmpty(top2))
			push(&top2,x);
		else
		{
			while((x < peek(top2)) && (!isEmpty(top2)))
			{
				int y = pop(&top2);
				push(&top,y);
			}
			push(&top2,x);
		}
	}
	
	printf("\n");
	printStack(top2);
	
}