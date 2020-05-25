/* C Program to Implement Queue  using Linked List */
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
 
struct node
{
    char str[20];
    struct node *next;
};
 
// Function to create a new node

struct node * createnode(char *data)
{
  
    struct node *temp = (struct node*) malloc(sizeof(struct node));
             strcpy(temp->str,data);
             temp->next = NULL;
    return temp;
}

// Function to insert in a queue

struct node * insertqueue(struct node *rear, char *data)
{
    struct node *temp = createnode(data);
     if (rear == NULL)
        rear = temp;
     else
      {
       
        rear->next = temp;
        rear = temp;
       }
 
  return rear;  
}
 
// Function to delete from a queue

// please note we have taken front poniter as double pointer because
// when we delete element the front will move to next node and 
//the change should be reflected to callong program also 

char * deletequeue(struct node **front)
{
    struct node *temp ;
    char *val = (char *) malloc(20);
     
     if (*front == NULL)
       {
            printf("Queue is empty in operation delete...");
            exit(0);
        }
     else
      {
        strcpy(val,(*front)->str);
        //printf("%s", val);
        temp = *front;       
        *front = (*front)->next; 
         free(temp);
        return val;
       }

}

/* Displaying the queue elements */
void display(struct node *front)
{
    struct node *front1 = front;
 
    if ((front1 == NULL))
    {
        printf("Queue is empty");
        return;
    }
    while (front1 != NULL)
    {
        printf("%s ", front1->str);
        front1 = front1->next;
    }
    
}
 
 
/* Returns the front element of queue without delete*/
char * frontelement(struct node *front)
{
    if ((front != NULL))
        return (front->str);
    else
        return "";
}
 
/* Display if queue is empty or not */
int  emptyqueue(struct node *front, struct node *rear)
{
     if ((front == NULL) && (rear == NULL))
        return 1;
    else
       return 0;
}