#include<bits/stdc++.h>
#define SS struct stackNode *
using namespace std;

struct stackNode{
    int data;
    struct stackNode * next;
};

SS createNode (int data)
{
    SS temp = new stackNode;
    temp->data = data;
    temp->next = NULL;
    return temp;
}

void push (SS *root,int data)
{
    SS newNode = createNode(data);
    newNode->next = *root;
    *root = newNode;
    cout<<"Element "<<data<<" Pushed in Stack"<<endl;
}

void pop(SS *root)
{
    if (*root == NULL)
    {
        cout<<"Stack is Empty "<<endl;
        return;
    }
    SS temp = *root;
    *root = (*root)->next;
    cout<<"Element "<<temp->data<<" Popped From Stack "<<endl;
    delete temp;
}

void displayStack (SS root)
{
    cout<<"Now Stack is :- "<<endl;
    while(root != NULL)
    {
        cout<<root->data<<" -> ";
        root = root->next;
    }
    cout<<endl;
}
int main()
{
    SS root = NULL;
    push(&root,10);
    push(&root,20);
    push(&root,30);
    push(&root,40);
    push(&root,50);
    displayStack(root);
    pop(&root);
    displayStack(root);
}
