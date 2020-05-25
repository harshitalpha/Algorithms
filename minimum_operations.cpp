#include <iostream>
using namespace std;

int solve(int n)
{
    int out = 0;
    while(n > 0)
    {
        if(n%2 == 0)
        {
            out = out + 1;
            n = n / 2;
        }
        else
        {
            out = out + 1;
            n = n -1;
        }
    }
    return out;
}

int main() {
	
	int t;
	cin>>t;
	while(t--)
	{
	    int n;
	    cin>>n;
	    int ans = solve(n);
	    cout<<ans<<endl;
	}
	return 0;
}
