// In 1 D array peak is that element which is grater the or equal to is neighbour
// I am using devide and conquer algo in this program 
// I am also showing simple algorithm in this program
#include<bits/stdc++.h>

using namespace std;

int find_peak_algo2(int arr[],int low, int high)
{
	if(low < high)
	{
		int mid = (low + high)/2;
		if(arr[mid] < arr[mid - 1])
			return find_peak_algo2(arr,low,mid-1);
		else if(arr[mid] < arr[mid + 1])
			return find_peak_algo2(arr,mid+1,high);
		else
			return mid;
	}
}

int simple(int arr[],int n)
{
	// simple loop will run 
	// no need to write the program
}

int main()
{
	int n;
	cout<<"Enter size :- ";
	cin>>n;
	int arr[n];
	cout<<"Enter array :- \n";
	for(int i = 0;i<n;i++)
		cin>>arr[i];
	int peak = find_peak_algo2(arr,0,n-1);
	cout<<"\n Peak Element is :- "<<arr[peak];
}
