
#include "avl.cpp"

int main()
{
	node * root = NULL;
	int arr[] = {50 , 40 , 30 , 20 , 10};
	int n = 5;
	root = insert_avl_array(arr,n);
	//root = insert_avl_node(root,60);
	print(root);
	
	//delete_node_avl(root,40);
	
	//cout<<endl;
	//print(root);
}