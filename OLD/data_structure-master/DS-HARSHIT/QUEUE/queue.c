#include<stdio.h>
#include<stdlib.h>
#define sq struct queue *
struct queue
{
    int data;
    struct queue * next;
};

struct queue * createNode(int data)
{
    struct queue * temp = (struct queue *)malloc(sizeof(struct queue));
    temp->data = data;
    temp->next = NULL;
    return temp;
}

void enqueue(sq *front,sq *rear,int data)
{
    sq newNode = createNode(data);
    if(*front == NULL && *rear == NULL)
        *front = *rear =newNode;
    else
    {
        (*rear)->next = newNode;
        *rear = newNode;
    }
}

void printQueue(struct queue *front , struct queue *rear)
{
    while(1)
    {
        printf("%d -> ",front->data);
        if(front == rear)
            break;
        front = front->next;
    }
}

int dequeue (sq * front)
{
    if(*front == NULL)
        return -101;
    sq temp = *front;
    *front = (*front)->next;
    int x = temp->data;
    free(temp);
    return x;
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
