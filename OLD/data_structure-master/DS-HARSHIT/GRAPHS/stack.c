#define ss struct stack *
struct stack
{
	int data;
	struct stack * next;
};

ss createNode(int data)
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

void push(ss * top,int data)
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


int pop(ss * top)
{
	if(isEmpty(*top))
		return -99;
	ss temp = *top;
	*top = (temp)->next;
	temp->next = NULL;
	int n = temp->data;
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
		printf("%d ->",top->data);
		top = top->next;
	}
}