#include "binarySearchTree.cpp"


node * right_rotate(node * root)
{
	node * newRoot = root->left;
	root->left = newRoot->right;
	newRoot->right = root;
	root->height = height(root);
	newRoot->height = height(newRoot);
	root->bf = balance_factor(root);
	newRoot->bf = balance_factor(newRoot);
	return newRoot;
}

node * left_rotate(node * root)
{
	node * newRoot = root->right;
	root->right = newRoot->left;
	newRoot->left = root;
	root->height = height(root);
	newRoot->height = height(newRoot);
	root->bf = balance_factor(root);
	newRoot->bf = balance_factor(newRoot);
	return newRoot;
}


node * balance_tree(node * root)
{	
	if(root == NULL)
		return NULL;
	if(root->left)
		root->left = balance_tree(root->left);
	if(root->right)
		root->right = balance_tree(root->right);
	if(root->bf > 1)
		{
			if( height(root->left->left) >= height(root->left->right))
			{
				root = right_rotate(root);
			}
			else
			{
				root->left = left_rotate(root->left);
				root = right_rotate(root);
			}
		}
		
		
	if(root->bf < -1)
		{
			if( height(root->right->right) >= height(root->right->left))
			{
				root = left_rotate(root);
			}
			else
			{
				root->right = right_rotate(root->right);
				root = left_rotate(root);
			}
		}
	return root;
	
}



node * insert_avl_array(int arr[] , int n)
{
	node * root = NULL;
	for(int i = 0;i<n;i++)
	{
		node * newNode = create_node(arr[i]);
		root = insert(root , newNode);
	}
	//root = balance_tree(root);
	//assign_height(root);
	return root;
}

node * insert_avl_node(node * root, int n)
{
	node * newNode = create_node(n);
	root = insert(root , newNode);
	root = balance_tree(root);
	//assign_height(root);
	return root;
}

node * delete_node_avl(node * root,int n)
{
	deleteNode(root,n);
	
	root = balance_tree(root);
	return root;
}

void print(node * root)
{
	inorder(root);
}
