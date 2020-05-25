#include <iostream>
#include <cmath>
using namespace std;

int main() {
	int t;
	cin>>t;
	while(t--)
	{
	    int n;
	    cin>>n;
	    float x = float(n)/9;
	    int up_bound = ceil(x);
	    int size = up_bound + n;
	    int A[size] = {0};
	    
	    for(int i = up_bound-1;i>=0;i--)
	    {
	        if(n > 9)
	        {
	            A[i] = 9;
	            n = n - 9;
	        }
	        else
	        {
	            A[i] = n;
	            break;
	        }
	    }
	    for(int i = 0;i<size;i++)
	    {
	        cout<<A[i];
	    }
	    cout<<endl;
	}
	return 0;
}
