#include<bits/stdc++.h>

using namespace std;

struct node {
    int data;
    struct node* next;
};


node *createNewNode(int n)     // it will create a new node
{
    node *newPtr = new node;
    newPtr->data = n;
    newPtr->next = NULL;
    return newPtr;
}


void Insert_beg(node** headder, node *n)       // it will insert new node in the linked list at the beginning
{
    if (*headder == NULL){
        *headder = n;
    }

    else
    {
        n->next = *headder;
        *headder = n;
    }
}


void split_list(node** evlist,node** odlist, node** head)
{   node * headder = *head;
    while(headder != NULL)
    {
        if(headder->data % 2 == 0)
        {
            node* newnode = createNewNode(headder->data);
            Insert_beg(evlist,newnode);
        }
        else
        {
            node* newnode = createNewNode(headder->data);
            Insert_beg(odlist,newnode);
        }
        headder = headder->next;
    }
}

void display(node* n)
{
    while(n!=NULL)
    {
        cout<<n->data<<"  ->  ";
        n = n->next;
    }
}


int main()
{
    node* head = NULL;
    node* evlist = NULL;
    node* odlist = NULL;

    node* nn1 = createNewNode(3);
    node* nn2 = createNewNode(5);
    node* nn3 = createNewNode(6);
    node* nn4 = createNewNode(2);

    Insert_beg(&head,nn1);
    Insert_beg(&head,nn2);
    Insert_beg(&head,nn3);
    Insert_beg(&head,nn4);

    display(head);

    split_list(&evlist,&odlist,&head);
    cout<<"\n";
    display(evlist);
    cout<<"\n";
    display(odlist);

}
