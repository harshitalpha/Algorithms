#include<stdio.h>
#include<stdlib.h>

struct AdjListNode
{
	int des;
	struct AdjListNode *next;
};

struct AdjList
{
	struct AdjListNode *head;
};

struct graph
{
	int v;
	struct AdjList *array;
};

struct AdjListNode * create_des_node (int des)
{
	struct AdjListNode * new_des = (struct AdjListNode *)malloc(sizeof(struct AdjListNode));
	new_des->des = des;
	new_des->next = NULL;
	return new_des;
}

struct graph * create_graph(int v)
{
	struct graph * new_graph = (struct graph *)malloc(sizeof(struct graph));
	
	new_graph->v = v;
	
	new_graph->array = (struct AdjList * )malloc(v * sizeof(struct AdjList));
	
	for(int i = 0;i<v;i++)
	{
		((new_graph->array)+i)->head = NULL;
	}
	
	return new_graph;
}

void add_edges(struct graph * graph, int src , int des)
{
	struct AdjListNode * new_node = create_des_node(des);
	new_node->next = ((graph->array)+src)->head;
	((graph->array)+src)->head = new_node;
	
	struct AdjListNode * new_node_src = create_des_node(src);
	new_node_src->next = ((graph->array)+des)->head;
	((graph->array)+des)->head = new_node_src;
}

void print_graph(struct graph * graph)
{
	for (int i = 0;i < graph->v;i++)
	{
		struct AdjListNode * temp = ((graph->array)+i)->head;
		printf("Adj List Of %d is \n",i);
		while(temp != NULL)
		{
			printf(" %d ->",temp->des);
			temp = temp->next;
		}
		printf("\n");
	}
}
void DFS (struct graph * graph , int s_ver)
{
	
}
void main()
{
	int v = 5;
	
	struct graph * graph = create_graph(v);
	
	add_edges(graph,0,1); 
	add_edges(graph,0,2);
	add_edges(graph,1,4);
	add_edges(graph,2,3);
	add_edges(graph,3,4);
	
	print_graph(graph);
	
}