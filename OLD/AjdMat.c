#include "queue.c"
void add_edge(int m[][50],int src,int des)
{
	m[src][des] = 1;
	m[des][src] = 1;
}

void BFS( int mat[][50], int n , sq *front, sq *rear , int visited [])
{
	if (isEmpty(front,rear))
		return;
	int v = dequeue(front);
	printf("%d ->",v);
	for(int i = 1; i<=n;i++)
	{
		if(mat[v][i] == 1 && visited[i] == 0)
		{
			visited[i] = 1;
			enqueue(front,rear,i);
		}
	}
	BFS(mat,n,front,rear,visited);
}
void printMat(int mat[][50],int n)
{
	for(int i = 1;i<=n;i++)
	{
		for(int j = 1;j<=n;j++)
			printf("%d ",mat[i][j]);
		printf("\n");
	}
}
void main()
{
	int mat[50][50] = {0};
	int no_ver = 7;
	add_edge(mat,1,2);
	add_edge(mat,1,7);
	add_edge(mat,1,3);
	add_edge(mat,2,7);
	add_edge(mat,2,3);
	add_edge(mat,3,6);
	add_edge(mat,3,5);
	add_edge(mat,3,4);
	add_edge(mat,4,5);
	add_edge(mat,4,6);
	add_edge(mat,5,6);
	add_edge(mat,6,7);
	
	int visited[8] = {0};
	sq front = NULL;
	sq rear = NULL;
	int v;
	printf("Enter Starting Vertex :- ");
	scanf("%d",&v);
	
	visited[v] = 1;
	enqueue(&front,&rear,v);
	
	BFS(mat,no_ver,&front,&rear,visited);
	
	//printMat(mat,no_ver);
}