#include<iostream>
#include<algorithm>
using namespace std;

struct node 
{
	int data;
	int height;
	int bf;
	node * left;
	node * right;
};

node * create_node(int data)
{
	node* newNode = new node;
	newNode->data = data;
	newNode->height = 1;
	newNode->bf = 0;
	newNode->left = NULL;
	newNode->right = NULL;
	return newNode;
}

int height(node * root)
{
	if(root == NULL)
		return 0;
	int lh,rh;
	if (root->left == NULL)
		lh = 0;
	else
		lh = root->left->height;
	if (root->right == NULL)
		rh = 0;
	else
		rh = root->right->height;
	if( lh > rh)
		return lh + 1; 
	else
		return rh + 1;
}

void inorder(node * root)
{
	if(root == NULL)
		return;
	inorder(root->left);
	cout<<root->data<<" "<<root->height<<" "<<root->bf<<" "<<"\n";
	inorder(root->right);
}

int balance_factor (node * root)
{	int bf = 0;
	if (root->right == NULL)
		bf = root->left->height;
	else if(root->left == NULL)
		bf = root->right->height;
	else
		bf = root->left->height - root->right->height;
	return bf;
}

node * insert(node * root,node * newNode)
{
	if (root ==NULL){
		return newNode;
	}
	else if(root->data < newNode->data)
	{
		root->right = insert(root->right , newNode);
	}
	else if(root->data > newNode->data)
	{
		root->left = insert(root->left , newNode);
	}
	root->height = height(root);
	root->bf = balance_factor(root);
	return root;
}
bool leaf(node * root)
{
	if(root->left == NULL && root->right == NULL)
		return true;
	else
		return false;
}

node * inorder_preceder(node * root)
{
	while(root->right != NULL)
		root = root->right;
	return root;
}

node * deleteNode(node * root , int data)
{
	if(root == NULL)
		return NULL;
	if(root->data < data)
		root->right = deleteNode(root->right , data);
	else if(root->data > data)
		root->left = deleteNode(root->left , data);
	else
		{
			if(leaf(root)){
				delete(root);
				return NULL;
			}
			else if( root->left == NULL){
				node * temp = root->right;
				delete(root);
				return temp;
			}
			else if( root->right == NULL){
				node * temp = root->left;
				delete(root);
				return temp;
			}
			else
			{
				node * temp = inorder_preceder(root->left);
				root->data = temp->data;
				root->left = deleteNode(root->left , temp->data);
			}
		}
}