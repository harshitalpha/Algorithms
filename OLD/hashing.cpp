#include<iostream>

using namespace std;

struct link_list
{
	int data;
	link_list * next;
};



struct hash_table
{
	int size;
	link_list * head;
};

link_list * create_node(int data)
{
	link_list * new_node = new link_list;
	new_node->data = data;
	new_node->next = NULL;
	return new_node;
}

hash_table * create_hash_table(int size)
{
	hash_table * new_hash = new hash_table;
	new_hash->size = size;
	
	new_hash->head = new link_list[size];
	
	for(int i = 0;i<size;i++)
	{
		new_hash->head[i].next = NULL;
	}
	return new_hash;
}

void insert(hash_table * hash_table , int val)

int main()
{
	int n;
	cout<<"Enter The Size Of Hash Table :- ";
	cin>>n;
	
	hash_table * hashTable = create_hash_table(n);
}