#include<iostream>

using namespace std;

struct AdjListNode
{
	int des;
	struct AdjListNode *next;
};

struct AdjList
{
	strcut AdjListNode *head;
};

struct graph
{
	int v;
	struct AdjList *array;
};

struct AdjListNode * create_des_node (int des)
{
	struct AdjListNode *
}