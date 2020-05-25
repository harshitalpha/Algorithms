#include<stdio.h>
#include<stdlib.h>
#include<ctype.h>
#include<string.h>
#define ss struct stack *
struct stack
{
	char *data;
	struct stack * next;
};

ss createNode(char data)
{
	ss temp = (struct stack *)malloc(sizeof(struct stack));
	temp->data = data;
	temp->next = NULL;
	return temp;
}
int isEmpty(ss top)
{
	return top == NULL ;
}

void push(ss * top,char data)
{
	ss newNode = createNode(data);
	if (*top == NULL)
		*top = newNode;
	else
	{
		newNode->next = *top;
		*top = newNode;
	}
	//printf("%d inserted in the stack \n",data);
}


char pop(ss * top)
{
	if(isEmpty(*top))
		return -99;
	ss temp = *top;
	*top = (temp)->next;
	temp->next = NULL;
	char n = temp->data;
	free(temp);
	return n;
}

int peek(ss top)
{
	return top->data;
}

void printStack(ss top)
{
	while(top != NULL)
	{
		printf("%c ->",top->data);
		top = top->next;
	}
}

int prec(char data)
{
	switch(data)
	{
		case '(' : return 0;
			   break;
		case '+' :
		case '-' : return 1;
			   break;
		case '*' :
		case '/' : return 2;
			   break;
		case '^' : return 3;
			   break;
	}
}

int main()
{
	ss top = NULL;


	char exp[50] = "a+b*c-d/e";
	int k = -1;
	char post[50];
	for(int i=0;i<strlen(exp);i++)
	{
		if(isalpha(exp[i]) || isdigit(exp[i]))
			post[++k] = exp[i];
		else if(exp[i] == '(')
			push(&top,exp[i]);
		else if(exp[i] == ')')
		{
			while(top->data != '(')
			{
				char x = pop(&top);
				post[++k] = x;
			}
			char garbage = pop(&top);
		}
		else
		{
			while(!isEmpty(top) && (prec(exp[i]) <= prec(top->data)))
			{
				char x = pop(&top);
				post[++k] = x;
			}
			push(&top,exp[i]);
		}
	}
	while(!isEmpty(top))
	{
		char x = pop(&top);
		post[++k] = x;
	}
	post[++k] = '\0';
	printf("\n%s",post);








}
