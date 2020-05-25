#include<bits/stdc++.h>
using namespace std;

struct node{
    int data;
    node *next;
};

node *head,*rear;

node *createNewNode(int n)     // it will create a new node
{
    node *newPtr = new node;
    newPtr->data = n;
    newPtr->next = NULL;
    return newPtr;
}


void Insert_beg(node *n)       // it will insert new node in the linked list at the beginning
{
    if (head == NULL){
        head = n;
        rear = n;
    }

    else
    {
        n->next = head;
        head = n;
    }
}

void Insert_end(node * n)       // it will insert new node in the linked list at the end
{
    if(head == NULL)
        head = rear = n;
    else
    {
        rear->next = n;
        rear = n;
    }
}

void Insert_after(node *n,int x)
{
    node *temp = head;
    while(temp->data != x  &&  temp->next!=NULL)
        temp = temp->next;
    if(temp->data == x)
    {
        n->next = temp->next;
        temp->next = n;
    }
    else
    {
        cout<<"Node Not Exist"<<endl;
        system("pause");
        exit(1);
    }
}

node *findNode(int d)
{
    node *temp = head;
    while(temp->data != d  &&  temp->next!=NULL)
        temp = temp->next;
    if(temp->data == d)
    {
        return temp;
    }
    else
    {
        return NULL;
    }
}

void deleteNode(node * n)
{
    node * temp = new node;
    temp = n->next;
    n->data = temp->data;
    n->next = temp->next;
    delete(temp);
}

void display(node * n)              // it will display the list
{
    while(n!=NULL)
    {
        cout<<n->data<<"  ->  ";
        n = n->next;
    }

}

int countNodeLoop(node *n)
{
    int c = 0;
    while(n->next != NULL)
    {
        c++;
        n = n->next;
    }
    return c;
}

int countNodeRecursion(node *n)
{
    if(n == NULL)
        return 0;
    return 1+countNodeRecursion(n->next);
}

int main()
{
    head = rear = NULL;
    // setting head as null
    int n;
    cout<<"Enter The value to insert in list at beginning :- \n";
    cin>>n;

    node *newNode = createNewNode(n);

    if(newNode != NULL)
    {
        cout<<"Successfully created a new node\n ";
        system("pause");
    }

    else
    {
        cout<<"Can not create node :- \n";
        system("pause");
        exit(1);
    }

    cout<<"Now inserting node at the beginning of list\n";
    system("pause");
    Insert_beg(newNode);

    cout<<"Now list is :- \n";
    display(head);




    cout<<"\n\n\n\nNow inserting Element at End of list :- ";
    system("pause");
    cout<<"Enter The value to insert in list at end :- ";
    cin>>n;

    node *newNodeEnd = createNewNode(n);

    if(newNodeEnd != NULL)
    {
        cout<<"Successfully created a new node\n ";
        system("pause");
    }

    else
    {
        cout<<"Can not create node :- \n";
        system("pause");
        exit(1);
    }

    cout<<"Now inserting node at the end of list\n";
    system("pause");
    Insert_end(newNodeEnd);


    cout<<"Now list is :- \n";
    display(head);





    cout<<"\n\n\n\nNow inserting Element after the given value of list :- ";
    system("pause");
    cout<<"Enter The value to insert in list  :- ";
    cin>>n;
    int x;
    cout<<"Enter The value after which "<<n<<" is inserted :- ";
    cin>>x;



    node *newNodeAfter = createNewNode(n);

    if(newNodeAfter != NULL)
    {
        cout<<"Successfully created a new node\n ";
        system("pause");
    }

    else
    {
        cout<<"Can not create node :- \n";
        system("pause");
        exit(1);
    }

    cout<<"Now inserting node after "<<x<<" of list\n";
    system("pause");
    Insert_after(newNodeAfter,x);


    cout<<"Now list is :- \n";
    display(head);
    system("pause");





    cout<<"\n\n\ndeNow Delete The Node from linked List :- ";
    cout<<"\nEnter The value to be deleted :- ";
    int d;
    cin>>d;
    node * dn = findNode(d);
    if(dn!=NULL)
    {
        cout<<"\nNode Find in Linked List :- ";
        cout<<"\nDeleting This Node ";
        system("pause");
        deleteNode(dn);
        cout<<"\nNow Link List Became : ";
        display(head);
        system("pause");
    }
    else
    {
        cout<<"\nERROR Node Not found !!!!";
        cout<<"\nExiting This Program !!";
        system("pause");
        exit(1);
    }




    cout<<"\n\n\nTill Now No. of element in link List : ";
    cout<<"\nVia Loop "<<countNodeLoop(head)+1;
    cout<<"\nVia Recursion "<<countNodeRecursion(head);
    system("pause");

}
