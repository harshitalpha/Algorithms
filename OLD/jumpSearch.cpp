#include<bits/stdc++.h>
using namespace std;

// for sorted array only
// time complexity = sqrt(n)

int jumpSearch(int a[],int n,int x)
{
    int m = sqrt(n);
    int p = 0;
    while(a[m-1]<x)
    {
        p = m;
        m = m + sqrt(n);
        if(p>=n)
            return -1;
    }
    for(int i=p;i<=m;i++)
    {
        if(a[i] == x)
            return i;
        return -1;
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
    int x = jumpSearch(a,n,k);
    if(x != -1)
        cout<<"Element Found at position "<<x+1;
    else
        cout<<"Element Not Found ";
}
