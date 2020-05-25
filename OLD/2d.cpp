// In 2 D array peak is that element which is grater the or equal to it's all neighbour
// I am using devide and conquer algo in this program 
// I am not showing simple algorithm in this program
#include<bits/stdc++.h>

using namespace std;

int find_max_index (int arr[][100],int n,int col)
{
	int max = 0;
	for(int i= 1;i<n;i++)
	{
		if(arr[i][col] > arr[max][col])
			max = i;
	}
	return max;
}

int find_peak(int arr[][100], int n,int m,int m_low,int m_high) 
{
	if(m_low <= m_high)
	{
		int mid_col = (m_low + m_high)/2;
		int max_index = find_max_index(arr,n,mid_col);
		if(mid_col>0 && arr[max_index][mid_col] < arr[max_index][mid_col-1])
			find_peak(arr,n,m,m_low,mid_col-1);
		else if(mid_col<m-1 && arr[max_index][mid_col] < arr[max_index][mid_col+1])
			find_peak(arr,n,m,mid_col+1,m_high);
		else
			return arr[max_index][mid_col];
	}
}

void print_matrix(int arr[][100] ,int n ,int m)
{
	for(int i=0;i<n;i++)
	{
		for(int j=0;j<m;j++)
			cout<<arr[i][j]<<" ";
		cout<<endl;
	}	
}

int main()
{
	int n;
	cout<<"Enter row :- ";
	cin>>n;
	int m;
	cout<<"Enter column :- ";
	cin>>m;
	int arr[n][100];
	cout<<"Enter array :- \n";
	for(int i = 0;i<n;i++)
		for(int j = 0;j<m;j++)
			cin>>arr[i][j];
	cout<<endl;
	print_matrix(arr,n,m);
	cout<<endl;
	cout<<"\n The Peak Element is :- "<<find_peak(arr,n,m,0,m-1);
}