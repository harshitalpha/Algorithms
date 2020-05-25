#include<bits/stdc++.h>
using namespace std;
struct node {
    int data;
    struct node * next;
};

node *createNewNode(int n)     // it will create a new node
{
    node *newPtr = new node;
    newPtr->data = n;
    newPtr->next = NULL;
    return newPtr;
}
