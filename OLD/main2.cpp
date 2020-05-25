#include "binarySearchTree.cpp"

int main()
{
	node * root = NULL;
	int arr[] = {5 , 4 , 3 , 9 , 7 , 13};
	int n = 6;
	for(int i = 0;i<n;i++)
	{
		node * newNode = create_node(arr[i]);
		root = insert(root,newNode);
	}
	node * newNode = create_node(50);
	root = insert(root,newNode);
	
	inorder(root);
	
	//deleteNode(root,5);
	
	//cout<<endl;
	//inorder(root);
}