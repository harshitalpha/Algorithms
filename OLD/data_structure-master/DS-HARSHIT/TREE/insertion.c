#include"queue.c"


struct treeNode
{
    int data;
    struct treeNode * left;
    struct treeNode * right;
};

struct treeNode *createTreeNode(int data)
{
    struct treeNode *temp = (struct treeNode *)malloc(sizeof(struct treeNode));
    temp->data = data;
    temp->left = NULL;
    temp->right = NULL;
    return temp;
}

void insertTreeNode(struct treeNode ** root,int data)
{
    sq front = NULL;
    sq rear = NULL;
    enqueue(&front,&rear,(*root));
    //printQueue(front,rear);
    while(!isempty(front,rear))
    {
        struct treeNode * temp = frontElement(front);

        if(temp->left == NULL){
            temp->left = createTreeNode(data);
            break;
        }else
            enqueue(&front,&rear,temp->left);

         if(temp->right == NULL){
            temp->right = createTreeNode(data);
            break;
        }else
            enqueue(&front,&rear,temp->right);
		
		dequeue(&front);
    }
}

void levelOrder(struct treeNode **root)
{
    sq front = NULL;
	sq rear = NULL;

	enqueue(&front,&rear,*root);
	//enqueue(&front,&rear,root->left);
	//enqueue(&front,&rear,root->right);

	while(!isempty(front,rear))
	{
		struct treeNode * temp = frontElement(front);
		printf(" %d -> ",temp->data);
		if(temp->left)
            enqueue(&front,&rear,temp->left);
        if(temp->right)
            enqueue(&front,&rear,temp->right);
		dequeue(&front);
	}
}

void inorder(struct treeNode* temp)
{
    if (!temp)
        return;

    inorder(temp->left);
    printf("%d - >  ",temp->data);
    inorder(temp->right);
}

int main()
{
    struct treeNode * root = createTreeNode(10);
    root->left = createTreeNode(11);
    root->left->left = createTreeNode(3);
    root->right = createTreeNode(9);
    root->right->left = createTreeNode(2);
    inorder(root);

    insertTreeNode(&root,12);
    printf("\n");
    levelOrder(&root);


	
}
