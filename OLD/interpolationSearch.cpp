#include<bits/stdc++.h>
using namespace std;

int interpolationSaerch(int a[],int n, int x)
{
    int lo = 0,hi = n-1;
    while(lo<=hi && x>=a[lo] && x<=a[hi])
    {
        if (lo == hi)
            if(a[lo] == x)
                return lo;
        int pos = lo + (((double)(hi-lo)/(a[hi] - a[lo])) * (x - a[lo]));
        if(a[pos] == x)
            return pos;
        else if(a[pos] < x)
            lo = pos + 1;
        else
            hi = pos - 1;

    }
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
    int x = interpolationSaerch(a,n,k);
    if(x != -1)
        cout<<"Element Found at position "<<x+1;
    else
        cout<<"Element Not Found ";
}
