#include<iostream>
using namespace std;

// only For Sorted Array
// time complexity = log(n)

int binarySearch(int a[],int l,int r,int k)
{
    while(l<=r)
    {
        int m = (l+r)/2;
        if(a[m] == k)
            return m;
        else if(a[m]<k)
            l = m+1;
        else
            r = m-1;
    }
    return -1;
}

int binarySearchRecursion(int a[],int l,int r,int k)
{
    if(l<=r)
    {
        int m = (l+r)/2;

        if(a[m] == k)
            return m;
        if(a[m]<k)
            return binarySearchRecursion(a,m+1,r,k);

        return binarySearchRecursion(a,l,m-1,k);
    }
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
    int x = binarySearch(a,0,n,k);
    int y = binarySearchRecursion(a,0,n,k);
    if(x != -1)
        cout<<"(iterative)Element Found at position "<<x+1<<"\n";
    else
        cout<<"Element Not Found \n";


    if(y != -1)
        cout<<"(recursive)Element Found at position "<<y+1;
    else
        cout<<"Element Not Found ";
}
