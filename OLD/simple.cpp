#include<bits/stdc++.h>
#define SN struct node*
using namespace std;

struct node {
    int data;
    struct node* next;
    struct node* prev;
};


SN createNewNode(int data)
{
    SN temp = new node;
    temp->data = data;
    temp->next = NULL;
    temp->prev = NULL;
    return temp;
}

void insert_beg (struct node** headder,SN* endp, struct node* newNode)
{
    if(*headder == NULL)
    {
        *headder = newNode;
        *endp = newNode;
    }
    else
    {
        (*headder)->prev = newNode;
         newNode->next = *headder;
         *headder = newNode;
    }
}

void display(SN headder,SN endp)
{
    while(true)
    {
        cout<<headder->data<<" ->  ";
        if(headder == endp)
            break;
        else
            headder = headder->next;
    }
}
void displayend(SN endp)
{
    while(endp != NULL){
        cout<<endp->data<<" ->   ";
        endp = endp->prev;
    }
}

void deleteNode(SN* headder, SN* endn, int data)
{
    if((*headder)->data == data)
    {
        SN temp = *headder;
        *headder = (*headder)->next;
        delete(temp);
    }
    else if((*endn)->data == data)
    {
        SN temp = *endn;
        *endn = temp->prev;
        delete(temp);
    }
    else
    {
        SN temp = *headder;
        while(temp->data != data  &&  temp->next!=NULL)
            temp = temp->next;
        if(temp->data == data)
        {
            temp->prev->next = temp->next;
            temp->next->prev = temp->prev;
            delete(temp);
        }
        else
        {
            cout<<"Node Not Exist"<<endl;
            system("pause");
            exit(1);
        }
    }
}

int main()
{
    SN head = NULL;
    SN endPointer = NULL;
    SN nn1 = createNewNode(4);
    SN nn2 = createNewNode(3);
    SN nn3 = createNewNode(2);
    insert_beg(&head,&endPointer,nn1);
    insert_beg(&head,&endPointer,nn2);
    insert_beg(&head,&endPointer,nn3);
    display(head,endPointer);
    cout<<"\n";
    displayend(endPointer);
    deleteNode(&head,&endPointer,4);
    cout<<"\n";
    display(head,endPointer);
}
