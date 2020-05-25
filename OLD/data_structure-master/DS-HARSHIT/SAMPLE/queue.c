#include<stdio.h>
#include<stdlib.h>
#include<stdbool.h>
#define sq struct queue *
struct queue
{
    int tnode;
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
        printf("%d -> ",front->tnode->data);
        if(front == rear)
            break;
        front = front->next;
    }
    printf("\n");
}*/

struct treeNode *dequeue (sq * front)
{
    if(*front == NULL)
        return NULL;
    struct treeNode *temp = (*front)->tnode;
    *front = (*front)->next;
    return temp;
}

bool isempty(struct queue * front,struct queue * rear)
{
    return (front = rear = NULL);
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
