#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>
#define sq struct queue *
struct queue
{
    struct treeNode * tnode;
    struct queue * next;
};

struct queue * createNode(struct treeNode *tnode)
{
    struct queue * temp = (struct queue *)malloc(sizeof(struct queue));
    temp->tnode = tnode;
    temp->next = NULL;
    return temp;
}

void enqueue(sq *front,sq *rear,struct treeNode *tNode)
{
    struct queue * newNode = createNode(tNode);
    if(*front == NULL && *rear == NULL){
        *front = *rear = newNode;
    }
    else
    {
        (*rear)->next = newNode;
        *rear = newNode;
    }
}

/*void printQueue(struct queue *front , struct queue *rear)
{   printf("\n");
    while(1)
    {
        struct treeNode * temp = front->tnode;
        printf("%d -> ",temp->data);
        if(front == rear)
            break;
        front = front->next;
    }
    printf("\n");
}*/

void dequeue (sq* front)
{
    if(*front == NULL)
        return NULL;
    struct queue *temp = *front;
    *front = (*front)->next;
	free(temp);
}

bool isempty(struct queue * front,struct queue * rear)
{
    return (front = rear = NULL);
}

struct treeNode * frontElement(sq front)
{
	struct treeNode * temp = front -> tnode;
	return temp;
}

/*int main()
{
    sq front = NULL;
    sq rear = NULL;
    enqueue(&front,&rear,10);
    enqueue(&front,&rear,20);
    enqueue(&front,&rear,30);
    printQueue(front,rear);
    int x = dequeue(&front);
    printf("\n%d Deleted from Queue\n ",x);
    printQueue(front,rear);
}
*/
