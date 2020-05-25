#include<stdio.h>
#include<stdlib.h>

struct node
{
	int data;
	struct node * next;
};

struct node * createNode(int data)
{
	struct node * temp = (struct node *)malloc(sizeof(struct node));
	temp->data = data;
	temp->next = temp;
	return temp;
}

void insertBegin(struct node ** head,struct node ** end,int data)
{
	struct node * newNode = createNode(data);
	if((*head) == NULL){
		(*head) = newNode;
		(*end) = newNode;
	}
	else
	{
		newNode->next = *head;
		(*end)->next = newNode;
		(*head) = newNode;
	}
}

void display(struct node * head,struct node * end)
{	do
	{
		printf(" %d -> ",head->data);
		head = head->next;
	}
	while(head != end);
}


void main()
{
	struct node * head = NULL;
	struct node * end = NULL;
	insertBegin(&head,&end,10);
	insertBegin(&head,&end,20);
	insertBegin(&head,&end,30);
	insertBegin(&head,&end,40);
	insertBegin(&head,&end,50);
	
	display(head,end);
}




























