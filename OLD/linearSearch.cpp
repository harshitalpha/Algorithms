#include<iostream>
using namespace std;

// time complexity =

int linearSearch(int a[],int n,int key)
{
    for(int i=0;i<n;i++)
        if(a[i] == key)
            return i;
    return -1;
}
int main()
{
    int n;
    cout<<"Enter the size of array :- ";
    cin>>n;
    int a[n];
    cout<<"Enter The Array :- \n";
    for(int i=0;i<n;i++)
        cin>>a[i];
    int k;
    cout<<"Enter The Element To be found :- ";
    cin>>k;
    int x = linearSearch(a,n,k);
    if(x != -1)
        cout<<"Element Found at position "<<x+1;
    else
        cout<<"Element Not Found ";
}
